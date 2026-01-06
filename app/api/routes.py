from fastapi import APIRouter
from app.core.parser import parse_logs

router = APIRouter()


@router.post("/format")
def format_logs(payload: dict):
    log_text = payload.get("log_text", "")
    parsed = parse_logs(log_text)
    return {"lines": parsed}
