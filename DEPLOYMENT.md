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

```text
https://mybinder.org/v2/gh/<GITHUB_USERNAME>/<REPO_NAME>/HEAD
```

Example:

```text
https://mybinder.org/v2/gh/your-username/Redrob-TalentGraphAI/HEAD
```

If you want Binder to open JupyterLab directly:

```text
https://mybinder.org/v2/gh/<GITHUB_USERNAME>/<REPO_NAME>/HEAD?urlpath=lab
```

## Command Reviewers Should Run

Inside Binder's terminal, run:

```bash
python rank.py \
  --candidates data/raw/candidates/candidates.jsonl \
  --jd data/raw/jd/job_description.docx \
  --out data/output/submission.csv
```

For a faster smoke test:

```bash
python rank.py \
  --candidates data/raw/candidates/candidates.jsonl \
  --jd data/raw/jd/job_description.docx \
  --out data/output/submission.csv \
  --limit 100
```

Then validate:

```bash
python data/raw/submission/validate_submission.py data/output/submission.csv
```

or use the internal validator automatically called by `rank.py`.

## Local Reproducibility

From a fresh local checkout:

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

## Submission Metadata

Use this as the reproduce command in the submission portal:

```bash
python rank.py --candidates data/raw/candidates/candidates.jsonl --jd data/raw/jd/job_description.docx --out data/output/submission.csv
```

Use the Binder URL as the sandbox link.

## Final Checklist

- Push the repository to GitHub.
- Confirm `requirements.txt` and `runtime.txt` are included.
- Open the Binder URL and wait for the environment to build.
- Run the smoke test with `--limit 100`.
- Run the full ranking command.
- Confirm `data/output/submission.csv` exists.
- Submit the GitHub repo link, Binder link, reproduce command, and CSV.
