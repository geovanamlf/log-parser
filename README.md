# Log Parser

Simple web application to parse and visualize application logs.

It processes raw log text, detects log levels (INFO, WARNING, ERROR), removes timestamps, and displays the result in a clean, color-coded interface.

Tech stack:
- Python
- FastAPI
- HTML / CSS / JavaScript

API:
POST /api/format

Request example:
{
  "log_text": "2026-01-05 10:32:10 INFO User logged in"
}

Running locally:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Live demo:
https://log-parser-m39o.onrender.com