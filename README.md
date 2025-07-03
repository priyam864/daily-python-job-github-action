# 🚀 GitHub Action: Daily Python Job

This project demonstrates how to run a Python script every day using **GitHub Actions** (a simple cron job automation).

## 📄 Files

| File | Description |
|------|-------------|
| `daily_task.py` | Python script that prints the current date & time |
| `.github/workflows/daily_job.yml` | GitHub Action workflow that runs daily |
| `README.md` | Setup & testing instructions |

---

## 🔧 How to Set Up

1. **Create a GitHub repository** (name: `daily-python-job-github-action`)
2. Push this folder structure to the repo
3. Go to the **Actions tab** — you'll see a workflow named `Daily Python Job`
4. It will run **daily at 6:00 AM UTC** (11:30 AM IST)
5. To test it immediately, click **"Run workflow"** from the GitHub UI

---

## ⏰ Schedule Info

- Uses [cron syntax](https://crontab.guru/) in GitHub Actions
- `'0 6 * * *'` = Run every day at 6:00 AM UTC (adjust if needed)

---

## ✅ Output Example

When the script runs, it will output something like:

```
✅ Daily job ran at 2025-07-03 11:30:00
```

---

## 💡 Bonus Ideas

- Log output to a file
- Send email via SMTP or Push Notification
- Store output in a database (SQLite or S3)

---
