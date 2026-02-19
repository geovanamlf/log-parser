from fastapi import APIRouter
from pydantic import BaseModel
from app.core.parser import parse_logs

router = APIRouter()


class LogRequest(BaseModel):
    log_text: str


@router.post("/format")
def format_logs(payload: LogRequest):
    parsed = parse_logs(payload.log_text)
    return {"lines": parsed}