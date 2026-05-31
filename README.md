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
