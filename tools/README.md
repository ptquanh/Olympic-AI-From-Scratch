# Curriculum tools

Only repeatable quality and review workflows belong in this directory:

- `audit_curriculum.py`: validate the manifest, chapter archetypes, exercises, references and notebook policy.
- `run_notebooks.py`: execute manifest notebooks without modifying their source files.
- `verify_notebook_report.py`: verify report coverage and notebook SHA-256 hashes.
- `merge_notebook_reports.py`: merge verified targeted reruns into a complete report.
- `build_review_records.py`: rebuild the human-readable 41-chapter review record.
- `promote_reviewed_statuses.py`: release-only status promotion using locally generated full-run evidence.

One-time content migration and notebook-generation scripts are intentionally not retained. All execution reports belong in `_dev/` as ignored CI/release artifacts. Routine pull requests execute only affected notebooks; scheduled and manual release runs cover the full manifest.
