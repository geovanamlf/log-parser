import re
from typing import List, Dict

TIMESTAMP_PATTERN = re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\s*')


def parse_logs(log_text: str) -> Dict:
    result = []

    lines = log_text.splitlines()

    for line in lines:
        if not line.strip():
            continue

        if "ERROR" in line:
            level = "ERROR"
        elif "WARNING" in line or "WARN" in line:
            level = "WARNING"
        elif "INFO" in line:
            level = "INFO"
        else:
            level = "UNKNOWN"

        message = line
        if level != "UNKNOWN":
            message = message.replace(level, "", 1).strip()

        message = TIMESTAMP_PATTERN.sub("", message).strip()

        result.append({
            "level": level,
            "message": message,
            "raw": line
        })

    summary = {
        "total": len(result),
        "info": sum(1 for r in result if r["level"] == "INFO"),
        "warning": sum(1 for r in result if r["level"] == "WARNING"),
        "error": sum(1 for r in result if r["level"] == "ERROR"),
        "unknown": sum(1 for r in result if r["level"] == "UNKNOWN"),
        "lines": result
    }

    return summary