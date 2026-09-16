#!/usr/bin/env python3
"""Audit every CSV while keeping names and email addresses out of analysis.

The script only emits aggregate counts, non-sensitive field headers, and CSV
row numbers. It does not print or write source row contents and does not alter
the raw CSV files.
"""

from __future__ import annotations

import argparse
import csv
import math
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


MISSING = {"", "na", "n/a", "nan", "null", "none", "missing", "unknown"}
EMAIL_RE = re.compile(r"\b[^\s@]+@[^\s@]+\.[^\s@]+\b", re.IGNORECASE)
DATE_RE = re.compile(r"date|time|week|month|year", re.IGNORECASE)
PII_RE = re.compile(
    r"(^|[_\-\s])(e[-_ ]?mail|email|name|first[-_ ]?name|last[-_ ]?name|full[-_ ]?name|respondent[-_ ]?name|customer[-_ ]?name|contact[-_ ]?name)([_\-\s]|$)",
    re.IGNORECASE,
)
FREE_TEXT_TOKENS = {"quote", "text", "notes", "comment", "description", "feedback", "verbatim"}
NUMERIC_RANGE_TOKENS = {
    "price", "cost", "spend", "revenue", "sales", "units", "reach", "engagement",
    "conversion", "margin", "cac", "ltv", "size", "volume", "count", "quantity",
    "acceptance", "intent",
}


def normalized_header(header: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", header.strip().lower()).strip("_")


def is_missing(value: str | None) -> bool:
    return value is None or value.strip().lower() in MISSING


def is_pii_header(file_name: str, header: str) -> bool:
    # The market context has geographic labels in a field named ``name``;
    # retain those public dimension labels while treating all other generic
    # name headers as sensitive by default.
    if file_name == "market_context.csv" and normalized_header(header) == "name":
        return False
    return bool(PII_RE.search(header))


def is_identifier_header(header: str) -> bool:
    return bool({"id", "identifier"} & set(normalized_header(header).split("_")))


def parse_number(value: str) -> float | None:
    cleaned = value.strip().replace(",", "")
    if cleaned.endswith("%"):
        cleaned = cleaned[:-1].strip()
    try:
        number = float(cleaned)
    except ValueError:
        return None
    return number if math.isfinite(number) else None


def percentile(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * fraction
    lower, upper = math.floor(position), math.ceil(position)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (position - lower)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]], list[int]]:
    rows: list[dict[str, str]] = []
    malformed: list[int] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        for row_number, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                malformed.append(row_number)
            rows.append({field: value or "" for field, value in row.items() if field is not None})
    return fields, rows, malformed


def compact_rows(rows: list[int]) -> str:
    if not rows:
        return ""
    ranges: list[str] = []
    start = previous = rows[0]
    for row in rows[1:]:
        if row == previous + 1:
            previous = row
        else:
            ranges.append(str(start) if start == previous else f"{start}–{previous}")
            start = previous = row
    ranges.append(str(start) if start == previous else f"{start}–{previous}")
    return ", ".join(ranges)


def date_invalid_rows(field: str, values: list[tuple[int, str]]) -> list[int]:
    """Check date-like fields only when their values look date-formatted."""
    if not DATE_RE.search(field):
        return []
    candidates = [(row, value.strip()) for row, value in values if not is_missing(value)]
    formatted = [value for _, value in candidates if re.search(r"[-/]", value)]
    if len(formatted) < max(2, len(candidates) // 2):
        return []
    invalid: list[int] = []
    for row, value in candidates:
        if not re.search(r"[-/]", value):
            continue
        try:
            datetime.fromisoformat(value.replace("/", "-"))
        except ValueError:
            invalid.append(row)
    return invalid


def grouping_fields(fields: list[str], numeric_fields: set[str], rows: list[dict[str, str]]) -> list[str]:
    dimensions: list[str] = []
    for field in fields:
        if field in numeric_fields or DATE_RE.search(field):
            continue
        values = {row.get(field, "").strip().casefold() for row in rows if not is_missing(row.get(field, ""))}
        if 1 < len(values) <= 20:
            dimensions.append(field)
    return dimensions


def grouped_iqr_outliers(
    indexed_values: list[tuple[int, float]], rows: list[dict[str, str]], dimensions: list[str]
) -> list[int]:
    groups: dict[tuple[str, ...], list[tuple[int, float]]] = defaultdict(list)
    for row_number, value in indexed_values:
        row = rows[row_number - 2]
        key = tuple(row.get(field, "").strip().casefold() for field in dimensions)
        groups[key].append((row_number, value))
    usable = [group for group in groups.values() if len(group) >= 8] or [indexed_values]
    outliers: list[int] = []
    for group in usable:
        values = [value for _, value in group]
        if len(values) < 8:
            continue
        q1, q3 = percentile(values, 0.25), percentile(values, 0.75)
        iqr = q3 - q1
        if iqr == 0:
            continue
        lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        outliers.extend(row for row, value in group if value < lower or value > upper)
    return sorted(set(outliers))


def audit_file(path: Path) -> dict:
    fields, rows, malformed = read_csv(path)
    pii_fields = [field for field in fields if is_pii_header(path.name, field)]
    identifiers = [field for field in fields if is_identifier_header(field)]
    analysis_fields = [field for field in fields if field not in pii_fields]

    # Remove entire email-bearing fields from the analysis even if the header
    # did not identify them. The count is retained only as an aggregate.
    email_cells: Counter[str] = Counter()
    for row in rows:
        for field in analysis_fields:
            value = row.get(field, "")
            if value and EMAIL_RE.search(value):
                email_cells[field] += 1
    email_fields = set(email_cells)
    analysis_fields = [field for field in analysis_fields if field not in email_fields]
    excluded_fields = sorted(set(pii_fields) | email_fields)
    free_text_fields = [
        field for field in analysis_fields
        if set(normalized_header(field).split("_")) & FREE_TEXT_TOKENS
    ]

    missing: dict[str, int] = {}
    invalid: dict[str, list[int]] = defaultdict(list)
    inconsistent: dict[str, dict[str, int]] = {}
    numeric: dict[str, list[tuple[int, float]]] = {}

    for field in analysis_fields:
        indexed = [(number, row.get(field, "")) for number, row in enumerate(rows, start=2)]
        present = [(number, value.strip()) for number, value in indexed if not is_missing(value)]
        if len(present) < len(rows):
            missing[field] = len(rows) - len(present)

        parsed = [(number, number_value) for number, value in present if (number_value := parse_number(value)) is not None]
        if present and len(parsed) / len(present) >= 0.9:
            numeric[field] = parsed
            invalid[field].extend(number for number, value in present if parse_number(value) is None)
        invalid[field].extend(date_invalid_rows(field, indexed))

        # Category consistency is about spelling/whitespace variants only;
        # values themselves are never emitted in the report.
        if present and field not in numeric:
            canonical: dict[str, set[str]] = defaultdict(set)
            for _, value in present:
                canonical[re.sub(r"\s+", " ", value).strip().casefold()].add(value)
            variants = [values for values in canonical.values() if len(values) > 1]
            if variants:
                inconsistent[field] = {
                    "groups": len(variants),
                    "variants": sum(len(values) for values in variants),
                }

    invalid = {field: sorted(set(numbers)) for field, numbers in invalid.items() if numbers}

    # Range checks are applied only to fields already inferred as numeric.
    for field, indexed_values in numeric.items():
        tokens = set(normalized_header(field).split("_"))
        for row_number, value in indexed_values:
            out_of_range = (
                ("age" in tokens and not 0 <= value <= 120)
                or (tokens & NUMERIC_RANGE_TOKENS and value < 0)
                or ("temperature" in tokens and not -100 <= value <= 70)
                or ("pct" in tokens and not 0 <= value <= 100)
            )
            if out_of_range:
                invalid.setdefault(field, []).append(row_number)
    invalid = {field: sorted(set(numbers)) for field, numbers in invalid.items() if numbers}

    duplicate_groups: dict[tuple[str, ...], list[int]] = defaultdict(list)
    for row_number, row in enumerate(rows, start=2):
        duplicate_groups[tuple(row.get(field, "").strip() for field in analysis_fields)].append(row_number)
    duplicate_rows = sorted(
        number for numbers in duplicate_groups.values() if len(numbers) > 1 for number in numbers[1:]
    )

    dimensions = grouping_fields(analysis_fields, set(numeric), rows)
    outliers: dict[str, list[int]] = {}
    for field, indexed_values in numeric.items():
        tokens = set(normalized_header(field).split("_"))
        distinct = {value for _, value in indexed_values}
        if (
            len(indexed_values) < 8
            or {"id", "identifier", "aware", "score", "rating", "flag"} & tokens
            or len(distinct) <= 2
        ):
            continue
        flagged = grouped_iqr_outliers(indexed_values, rows, dimensions)
        if flagged:
            outliers[field] = flagged

    issue_fields = set(missing) | set(invalid) | set(inconsistent) | set(outliers)
    safe_direct = not (
        excluded_fields or identifiers or free_text_fields or malformed or duplicate_rows
        or missing or invalid or inconsistent or outliers
    )
    return {
        "file": path.name,
        "rows": len(rows),
        "analysis_columns": len(analysis_fields),
        "excluded_fields": excluded_fields,
        "email_cells": sum(email_cells.values()),
        "identifiers": identifiers,
        "free_text_fields": free_text_fields,
        "malformed": malformed,
        "duplicate_groups": sum(len(numbers) > 1 for numbers in duplicate_groups.values()),
        "duplicate_rows": duplicate_rows,
        "missing": missing,
        "invalid": invalid,
        "inconsistent": inconsistent,
        "outliers": outliers,
        "issue_fields": sorted(issue_fields),
        "safe_direct": safe_direct,
    }


def build_report(results: list[dict]) -> str:
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    safe = [result["file"] for result in results if result["safe_direct"]]
    lines = [
        "# LUMEN data-quality report",
        "",
        f"Generated: {generated}",
        "",
        "## Scope and privacy guardrail",
        "",
        "Every CSV under `data/` was audited. Name/email-style fields and any email-bearing fields were excluded before quality metrics were calculated. No source row contents or personal values are reproduced in this report.",
        "",
        "| File | Rows | Non-PII columns analysed | Duplicate groups | Missing cells | Invalid cells | Category variant groups | Outlier fields | Direct use |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for result in results:
        lines.append(
            f"| `{result['file']}` | {result['rows']} | {result['analysis_columns']} | {result['duplicate_groups']} | {sum(result['missing'].values())} | {sum(len(numbers) for numbers in result['invalid'].values())} | {sum(details['groups'] for details in result['inconsistent'].values())} | {len(result['outliers'])} | {'Yes' if result['safe_direct'] else 'No'} |"
        )
    lines.extend(["", "### Files safe to use directly", ""])
    lines.extend((f"- `{file}`" for file in safe)) if safe else lines.append("None.")

    lines.extend([
        "",
        "## Cleaning decisions",
        "",
        "1. Treat blank strings and the case-insensitive tokens `NA`, `N/A`, `NaN`, `NULL`, `None`, `missing`, and `unknown` as missing.",
        "2. Exclude all name/email-style fields and any field containing an email address from analysis, joins, exports, charts, and models. The report names sensitive headers only so analysts know what to drop; it never includes their values.",
        "3. Treat `*_id`/identifier fields as privacy risks for sharing. They may be retained temporarily for row-grain or deduplication checks, then dropped or hashed before distribution.",
        "4. Detect duplicates using the remaining fields; keep the first occurrence and quarantine subsequent row numbers until the source event grain is confirmed.",
        "5. Detect category inconsistencies only when values differ by case or whitespace. Standardise after confirming the intended category; do not silently merge distinct categories.",
        "6. Infer numeric fields only when at least 90% of non-missing values parse as numbers. Flag malformed numeric/date values and simple domain violations (negative measures, age outside 0–120, temperature outside −100–70, percentage outside 0–100).",
        "7. For continuous numeric measures, flag Tukey 1.5×IQR outliers with at least eight observations, grouped by stable low-cardinality dimensions when possible. Skip identifiers, binary flags, awareness indicators, and bounded rating scales. Outliers are review flags, not automatic deletions.",
        "8. Treat free-text fields as requiring a manual privacy review before external sharing, even when automated email detection finds nothing.",
        "9. A file is marked **Yes** for direct use only when it has no detected PII, identifier/free-text privacy risk, malformed rows, duplicates, missing values, category variants, invalid values, or statistical outliers.",
        "",
        "## File-by-file actions",
        "",
    ])

    for result in results:
        lines.extend([f"### `{result['file']}`", ""])
        privacy = []
        if result["excluded_fields"]:
            fields = ", ".join(f"`{field}`" for field in result["excluded_fields"])
            privacy.append(f"drop sensitive fields {fields} ({result['email_cells']} email-bearing cell(s) detected)")
        if result["identifiers"]:
            fields = ", ".join(f"`{field}`" for field in result["identifiers"])
            privacy.append(f"drop or hash identifiers before sharing: {fields}")
        if result["free_text_fields"]:
            fields = ", ".join(f"`{field}`" for field in result["free_text_fields"])
            privacy.append(f"manually review free-text fields before sharing: {fields}")
        lines.append(f"- Privacy: {'; '.join(privacy) + '.' if privacy else 'No automated privacy risk detected.'}")
        lines.append(f"- Direct-use status: **{'Safe' if result['safe_direct'] else 'Not safe without review/cleaning'}**.")
        if result["malformed"]:
            lines.append(f"- Malformed CSV rows to fix: {compact_rows(result['malformed'])}.")
        if result["duplicate_rows"]:
            lines.append(f"- Duplicate rows to quarantine pending confirmation: {compact_rows(result['duplicate_rows'])}.")
        if result["missing"]:
            details = ", ".join(f"`{field}` {count} ({count / result['rows']:.1%})" for field, count in sorted(result["missing"].items()))
            lines.append(f"- Missing cells: {details}.")
        if result["invalid"]:
            details = ", ".join(f"`{field}` rows {compact_rows(rows)}" for field, rows in sorted(result["invalid"].items()))
            lines.append(f"- Invalid values: {details}. Repair from the source or exclude those rows from calculations.")
        if result["inconsistent"]:
            details = ", ".join(f"`{field}` ({info['groups']} group(s), {info['variants']} spelling variant(s))" for field, info in sorted(result["inconsistent"].items()))
            lines.append(f"- Category variants to standardise: {details}.")
        if result["outliers"]:
            details = ", ".join(f"`{field}` rows {compact_rows(rows)}" for field, rows in sorted(result["outliers"].items()))
            lines.append(f"- Outliers to review, not automatically delete: {details}.")
        if not any((result["malformed"], result["duplicate_rows"], result["missing"], result["invalid"], result["inconsistent"], result["outliers"], result["excluded_fields"], result["identifiers"], result["free_text_fields"])):
            lines.append("- No data-quality exception detected.")
        lines.append("")

    lines.extend([
        "## Analyst checklist",
        "",
        "- Drop all listed sensitive fields and email-bearing fields before analysis or sharing.",
        "- Drop/hash identifiers and manually review free text before external distribution.",
        "- Quarantine duplicate and invalid-value rows listed above; do not remove outliers without business validation.",
        "- Resolve missingness based on business meaning; do not replace missing with zero unless zero is the defined meaning.",
        "- Re-run `python3 scripts/audit_data_quality.py` after cleaning changes.",
        "",
        "## Reproducibility",
        "",
        "```bash",
        "python3 scripts/audit_data_quality.py",
        "```",
        "",
        "The script writes `DATA_QUALITY_REPORT.md`, never modifies raw CSVs, and never prints source row contents.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--output", type=Path, default=Path("DATA_QUALITY_REPORT.md"))
    args = parser.parse_args()
    csv_paths = sorted(path for path in args.data_dir.glob("*.csv") if path.is_file())
    if not csv_paths:
        raise SystemExit(f"No CSV files found under {args.data_dir}")
    results = [audit_file(path) for path in csv_paths]
    args.output.write_text(build_report(results), encoding="utf-8")
    print(f"Audited {len(results)} CSV files; report written to {args.output}")
    print(f"Files marked safe for direct use: {sum(result['safe_direct'] for result in results)}")


if __name__ == "__main__":
    main()
