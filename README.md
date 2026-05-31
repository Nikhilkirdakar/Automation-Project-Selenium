# PythonSelenium - Commerce

This repository contains pytest-based Selenium tests for the Sauce Demo sample site.

Setup

1. Create a virtual environment: python -m venv .venv
2. Activate it: .venv\Scripts\activate
3. Install dependencies: pip install -r requirements.txt

Run tests

- Run default tests (uses Chrome by default):
  pytest -q

- Run headless on Chrome:
  pytest -q --headless --browser_name=chrome

Notes

- Tests use webdriver-manager to automatically download browser drivers.
- CI is provided in .github/workflows to run tests on push/PR.

Jenkins

This repository includes a Jenkinsfile to run tests on a schedule. The pipeline is configured to run once every morning (cron: H 6 * * *).

To create a Jenkins Pipeline job pointing to this repository, either:

1) Manually: Create a new Pipeline job in Jenkins, set Pipeline script from SCM -> Git -> Repository URL, and set Script Path to Jenkinsfile. Configure Build Triggers -> Build periodically with the desired cron.

2) Automatically: Use the provided helper script scripts/jenkins_create_job.sh. Example usage:

export JENKINS_URL="https://jenkins.example.com"
export JENKINS_USER="admin"
export JENKINS_TOKEN="<api-token>"
export JOB_NAME="python-selenium-daily"
export GIT_REPO="https://github.com/Nikhilkirdakar/Automation-Project-Selenium.git"
./scripts/jenkins_create_job.sh

The helper script uses the Jenkins REST API and requires curl and Python to be available. Store credentials securely (e.g. as Jenkins credentials) when configuring automated creation.


Notifications

- Jenkins: set SLACK_WEBHOOK (Incoming Webhook URL) and/or EMAIL_RECIPIENTS environment variables in the job or global Jenkins credentials. The pipeline will send a Slack message and email after each run.

Releases

- To create a release tag locally and push to GitHub:
  git tag -a v1.1.0 -m "Release v1.1.0"
  git push origin v1.1.0

