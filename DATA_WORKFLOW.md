# LUMEN data workflow

## Mandatory quality gate

Before using any CSV in `data/`, run:

```bash
python3 scripts/audit_data_quality.py
```

Then read [`DATA_QUALITY_REPORT.md`](DATA_QUALITY_REPORT.md). The report is regenerated from the current files and records the exact rows and fields that need review.

## Privacy rules

- Never use or export name/email values. The audit excludes those fields before calculating metrics and never prints their contents.
- Drop or hash identifier fields such as `respondent_id` before sharing data outside the analysis workspace.
- Manually review free-text fields such as quotes and notes for personal information before sharing them.
- Do not commit cleaned or derived files that contain personal values.

## File-use rules

Files marked **Direct use: Yes** in the report have no detected quality or automated privacy exception under the audit rules. Every other file requires the documented cleaning or review step first. Duplicate and invalid-value rows should be quarantined, missing values handled according to business meaning, and statistical outliers validated rather than deleted automatically.

After any data or audit-rule change, rerun the script and review the updated report before using the data again.
