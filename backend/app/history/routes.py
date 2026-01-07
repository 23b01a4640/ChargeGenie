from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.jwt import decode_token
from app.history.models import ChargingHistoryCreate
from app.history.service import create_history_entry, get_user_history

router = APIRouter(prefix="/history", tags=["Charging History"])
security = HTTPBearer()


@router.post("/")
def save_history(
    payload: ChargingHistoryCreate,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = decode_token(credentials.credentials)
    create_history_entry(token["user_id"], payload.dict())
    return {"status": "saved"}


@router.get("/me")
def my_history(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = decode_token(credentials.credentials)
    return get_user_history(token["user_id"])
