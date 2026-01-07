from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.jwt import decode_token
from app.stations.models import StationUpdate
from app.stations.service import get_station_by_owner, upsert_station

router = APIRouter(prefix="/stations", tags=["Stations"])
security = HTTPBearer()


@router.get("/me")
def get_my_station(credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = decode_token(credentials.credentials)

    if payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admins only")

    station = get_station_by_owner(payload["user_id"])
    return station or {}


@router.put("/me")
def update_my_station(
    update: StationUpdate,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    payload = decode_token(credentials.credentials)

    if payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admins only")

    upsert_station(payload["user_id"], update.dict())
    return {"status": "updated"}
