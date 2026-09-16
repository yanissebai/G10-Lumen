# LUMEN data-quality report

Generated: 2026-09-14 16:06 UTC

## Scope and privacy guardrail

Every CSV under `data/` was audited. Name/email-style fields and any email-bearing fields were excluded before quality metrics were calculated. No source row contents or personal values are reproduced in this report.

| File | Rows | Non-PII columns analysed | Duplicate groups | Missing cells | Invalid cells | Category variant groups | Outlier fields | Direct use |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `channel_economics.csv` | 6 | 8 | 0 | 0 | 0 | 0 | 0 | Yes |
| `competitor_price_history.csv` | 48 | 6 | 0 | 0 | 0 | 0 | 2 | No |
| `competitor_prices_by_channel.csv` | 27 | 6 | 0 | 0 | 0 | 0 | 0 | Yes |
| `cost_breakdown.csv` | 7 | 3 | 0 | 1 | 0 | 0 | 0 | No |
| `customer_quotes.csv` | 12 | 3 | 0 | 0 | 0 | 0 | 0 | No |
| `customer_survey.csv` | 420 | 13 | 0 | 0 | 0 | 0 | 5 | No |
| `historical_sales_weekly.csv` | 706 | 6 | 4 | 0 | 0 | 0 | 2 | No |
| `market_context.csv` | 36 | 7 | 0 | 0 | 0 | 0 | 0 | No |
| `marketing_funnel_monthly.csv` | 72 | 8 | 0 | 0 | 0 | 0 | 4 | No |
| `price_sensitivity_survey.csv` | 300 | 6 | 0 | 0 | 0 | 0 | 4 | No |
| `price_test_results.csv` | 9 | 6 | 0 | 0 | 0 | 0 | 1 | No |
| `seasonality_and_weather.csv` | 12 | 3 | 0 | 0 | 0 | 0 | 0 | Yes |

### Files safe to use directly

- `channel_economics.csv`
- `competitor_prices_by_channel.csv`
- `seasonality_and_weather.csv`

## Cleaning decisions

1. Treat blank strings and the case-insensitive tokens `NA`, `N/A`, `NaN`, `NULL`, `None`, `missing`, and `unknown` as missing.
2. Exclude all name/email-style fields and any field containing an email address from analysis, joins, exports, charts, and models. The report names sensitive headers only so analysts know what to drop; it never includes their values.
3. Treat `*_id`/identifier fields as privacy risks for sharing. They may be retained temporarily for row-grain or deduplication checks, then dropped or hashed before distribution.
4. Detect duplicates using the remaining fields; keep the first occurrence and quarantine subsequent row numbers until the source event grain is confirmed.
5. Detect category inconsistencies only when values differ by case or whitespace. Standardise after confirming the intended category; do not silently merge distinct categories.
6. Infer numeric fields only when at least 90% of non-missing values parse as numbers. Flag malformed numeric/date values and simple domain violations (negative measures, age outside 0–120, temperature outside −100–70, percentage outside 0–100).
7. For continuous numeric measures, flag Tukey 1.5×IQR outliers with at least eight observations, grouped by stable low-cardinality dimensions when possible. Skip identifiers, binary flags, awareness indicators, and bounded rating scales. Outliers are review flags, not automatic deletions.
8. Treat free-text fields as requiring a manual privacy review before external sharing, even when automated email detection finds nothing.
9. A file is marked **Yes** for direct use only when it has no detected PII, identifier/free-text privacy risk, malformed rows, duplicates, missing values, category variants, invalid values, or statistical outliers.

## File-by-file actions

### `channel_economics.csv`

- Privacy: No automated privacy risk detected.
- Direct-use status: **Safe**.
- No data-quality exception detected.

### `competitor_price_history.csv`

- Privacy: No automated privacy risk detected.
- Direct-use status: **Not safe without review/cleaning**.
- Outliers to review, not automatically delete: `list_price_eur` rows 39–40, 45, `shelf_price_eur` rows 39–40, 45.

### `competitor_prices_by_channel.csv`

- Privacy: No automated privacy risk detected.
- Direct-use status: **Safe**.
- No data-quality exception detected.

### `cost_breakdown.csv`

- Privacy: No automated privacy risk detected.
- Direct-use status: **Not safe without review/cleaning**.
- Missing cells: `pct_of_total` 1 (14.3%).

### `customer_quotes.csv`

- Privacy: manually review free-text fields before sharing: `quote`.
- Direct-use status: **Not safe without review/cleaning**.

### `customer_survey.csv`

- Privacy: drop sensitive fields `email`, `first_name`, `last_name` (0 email-bearing cell(s) detected); drop or hash identifiers before sharing: `respondent_id`.
- Direct-use status: **Not safe without review/cleaning**.
- Outliers to review, not automatically delete: `age` rows 18, 33, 273, 324, 331, `lumen_purchase_intent_1_10` rows 5, 71, 112, 123, 148, 182, 193, 218, 334, 357, 374, 403, `monthly_beverage_spend_eur` rows 19, 107, 112, 129, 183, 312, 314, 326, 331, 353, 372, 381, `price_sensitivity_1_10` rows 31, 113, 120, 131, 197, 201, 295, 314, 333–334, 357–358, `purchase_frequency_per_month` rows 42, 112, 123, 165, 201, 268, 273, 307, 316.

### `historical_sales_weekly.csv`

- Privacy: No automated privacy risk detected.
- Direct-use status: **Not safe without review/cleaning**.
- Duplicate rows to quarantine pending confirmation: 704–707.
- Outliers to review, not automatically delete: `revenue_eur` rows 266, 268–269, 271, 665, 669, 673, 675, 680–681, 683–684, 690–692, 696, `units_sold` rows 268, 271, 665, 669, 673, 680–681, 683, 687, 691–692, 696.

### `market_context.csv`

- Privacy: manually review free-text fields before sharing: `notes`.
- Direct-use status: **Not safe without review/cleaning**.

### `marketing_funnel_monthly.csv`

- Privacy: No automated privacy risk detected.
- Direct-use status: **Not safe without review/cleaning**.
- Outliers to review, not automatically delete: `conversions_customers_acquired` rows 19, `engagements` rows 19, `reach` rows 19, `spend_eur` rows 19, 26, 35.

### `price_sensitivity_survey.csv`

- Privacy: drop or hash identifiers before sharing: `respondent_id`.
- Direct-use status: **Not safe without review/cleaning**.
- Outliers to review, not automatically delete: `cheap_eur` rows 16, 49, 108, 165, 168, 204, 247, `expensive_eur` rows 165, 200, `too_cheap_eur` rows 16, 134, 177, `too_expensive_eur` rows 65, 82, 150, 255, 257.

### `price_test_results.csv`

- Privacy: No automated privacy risk detected.
- Direct-use status: **Not safe without review/cleaning**.
- Outliers to review, not automatically delete: `contribution_margin_pct` rows 3.

### `seasonality_and_weather.csv`

- Privacy: No automated privacy risk detected.
- Direct-use status: **Safe**.
- No data-quality exception detected.

## Analyst checklist

- Drop all listed sensitive fields and email-bearing fields before analysis or sharing.
- Drop/hash identifiers and manually review free text before external distribution.
- Quarantine duplicate and invalid-value rows listed above; do not remove outliers without business validation.
- Resolve missingness based on business meaning; do not replace missing with zero unless zero is the defined meaning.
- Re-run `python3 scripts/audit_data_quality.py` after cleaning changes.

## Reproducibility

```bash
python3 scripts/audit_data_quality.py
```

The script writes `DATA_QUALITY_REPORT.md`, never modifies raw CSVs, and never prints source row contents.
