# Compliance Document Expiry Tracker | Python Compliance Automation
Python tool to monitor expiry dates for compliance certificates, policies, staff training records and regulatory documents.
Automatically flag documents nearing expiry and generate a compliance alert report for the compliance team review.

## 🛡️ Data Privacy & PII Protection
1. Only anonymized dummy test dataset is committed to GitHub. Real production records containing staff names, employee IDs or third-party PII are stored locally and never pushed to GitHub.
2. Identifiers in the sample dataset are masked. Production data can separate personal identifiers into a secured local folder.
3. .gitignore blocks any real confidential document logs (`*_real_document*.csv`) to prevent accidental upload.
4. Generated alert reports saved locally only; no confidential document content stored in exported files.
5. No sensitive document content is stored, only metadata (document ID, type, expiry date) for expiry monitoring.

## Project Objective
Compliance teams manage hundreds of certificates, policies and mandatory training records. This script automates monitoring: identify documents expiring within a defined window and output alert list for follow-up. Reduce manual spreadsheet checking.

## Features
- Load document metadata CSV
- Filter records to identify upcoming expiry
- Generate prioritized alert list (Critical / Warning / OK)
- Export alert report CSV for compliance meeting review
- Audit log of generated alerts

## Tech Stack
Python, pandas

## How to Run
```bash
pip install pandas
python document_expiry_tracker.py
