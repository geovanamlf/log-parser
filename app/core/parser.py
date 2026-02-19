import re
from typing import List, Dict

TIMESTAMP_PATTERN = re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\s*')

def parse_logs(log_text: str) -> List[Dict[str, str]]:
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

        item = {
            "level": level,
            "message": message,
            "raw": line
        }

        result.append(item)

    return result