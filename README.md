# log-parser

A simple web application to parse and visualize application logs.

It processes raw log text, detects log levels (INFO, WARNING, ERROR), removes timestamps, and displays the result in a clean, color-coded interface with a summary of occurrences by level.

## Tech stack

- Python
- FastAPI
- Jinja2
- HTML / CSS / JavaScript

## Project structure
```
app/
├── api/
│   └── routes.py       # API endpoints
├── core/
│   └── parser.py       # Log parsing logic
└── web/
    ├── static/
    │   └── style.css
    └── templates/
        └── index.html
tests/
└── test_parser.py
```

## API

`POST /api/format`

Request:
```json
{
  "log_text": "2026-01-05 10:32:10 INFO User logged in"
}
```

Response:
```json
{
  "total": 1,
  "info": 1,
  "warning": 0,
  "error": 0,
  "unknown": 0,
  "lines": [
    {
      "level": "INFO",
      "message": "User logged in",
      "raw": "2026-01-05 10:32:10 INFO User logged in"
    }
  ]
}
```

## Running locally
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

## Running tests
```bash
pytest tests/ -v
```

## Live demo

https://log-parser-m39o.onrender.com
