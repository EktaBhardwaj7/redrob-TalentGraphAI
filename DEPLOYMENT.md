# Deployment And Reproducibility Guide

## Recommended Platform: Binder

This project is best deployed as a reproducible Binder environment because it is a command-line Python ranker, not a web application. Binder can launch the GitHub repository in a clean Linux environment, install `requirements.txt`, and let reviewers run the same commands used locally.

## What Binder Needs

Binder uses these files automatically:

| File | Purpose |
|---|---|
| `requirements.txt` | Installs Python dependencies. |
| `runtime.txt` | Requests Python 3.11. |
| `README.md` | Gives reviewers the quick-start commands. |
| `rank.py` | Main reproducibility entry point. |

No GPU is required. No network calls are made during ranking.

## Binder Link Format

After pushing this repository to GitHub, create a Binder link in this format:

```
https://mybinder.org/v2/gh/EktaBhardwaj7/redrob-TalentGraphAI/HEAD
```
If you want Binder to open JupyterLab directly:

```
https://mybinder.org/v2/gh/<EktaBhardwaj7>/<redrob-TalentGraphAI>/HEAD?urlpath=lab
```
Command Reviewers Should Run
Inside Binder's terminal, run the following command to rank all candidates in the sample file (provided as sample_candidates.jsonl). The sample is small enough to run quickly without any --limit argument.

```bash
python rank.py \
  --candidates data/raw/candidates/sample_candidates.jsonl \
  --jd data/raw/jd/job_description.docx \
  --out data/output/test_submission.csv
  ```
This will generate test_submission.csv containing the ranked results for the sample.

To validate the output (checks correct format and rank coverage), run:
```bash
python data/raw/submission/validate_submission.py data/output/test_submission.csv
```
The rank.py script also automatically invokes the validator after writing the CSV, so you may see validation output directly.

Note: The sample file contains a small number of candidates (currently ~50). Do not use --limit with a value larger than the file size, or validation will fail (it expects exactly that many rows). If you need to test with fewer candidates, you can set --limit N where N is less than or equal to the total entries in the sample.

Local Reproducibility
From a fresh local checkout (using the full candidates.jsonl file, not the sample):
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python rank.py --candidates data/raw/candidates/candidates.jsonl --jd data/raw/jd/job_description.docx --out data/output/submission.csv
```
On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python rank.py --candidates data/raw/candidates/candidates.jsonl --jd data/raw/jd/job_description.docx --out data/output/submission.csv
```
