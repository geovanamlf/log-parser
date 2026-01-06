def parse_logs(log_text: str):
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

        parts = message.split()
        if len(parts) >= 3 and "-" in parts[0] and ":" in parts[1]:
            message = " ".join(parts[2:])

        item = {
            "level": level,
            "message": message,
            "raw": line
        }

        result.append(item)

    return result

