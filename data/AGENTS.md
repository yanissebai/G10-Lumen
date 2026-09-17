# Data quality gate

These instructions apply whenever Codex reads, analyses, creates, or modifies a file under `data/`.

Before using any CSV:

1. Read the root [`DATA_QUALITY_REPORT.md`](../DATA_QUALITY_REPORT.md) and [`data/README_data.md`](README_data.md).
2. Run `python3 scripts/audit_data_quality.py` from the repository root and review the regenerated report.
3. Treat the report's exclusions as mandatory: never use or reproduce name/email values, drop or hash identifier fields before sharing, and manually review free-text fields for personal data.
4. Use only files marked `Direct use: Yes` without additional cleaning. For every other file, apply the documented row/field exclusions or obtain business validation before modelling.
5. Do not write cleaned or derived datasets containing personal values into the repository.
6. After changing a data file or cleaning rule, rerun the audit and update the report if the findings change.

The report is the source of truth for the current dataset; this gate makes the workflow explicit for future Codex tasks and analysts.
