from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.jwt import decode_token
from app.core.database import db
from app.vehicle.models import VehicleCreate

router = APIRouter(prefix="/vehicle", tags=["Vehicle"])
security = HTTPBearer()


# 🔹 GET /vehicle/me
@router.get("/me")
def get_my_vehicle(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = decode_token(credentials.credentials)
    user_id = token["user_id"]

    vehicle = db.vehicles.find_one({"user_id": user_id})

    if not vehicle:
        return {}

    # ✅ SAFE JSON RESPONSE (NO ObjectId)
    return {
        "range_km": vehicle.get("range_km"),
        "battery_percent": vehicle.get("battery_percent"),
    }


# 🔹 PUT /vehicle/me
@router.put("/me")
def update_my_vehicle(
    payload: VehicleCreate,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = decode_token(credentials.credentials)
    user_id = token["user_id"]

    db.vehicles.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "range_km": payload.range_km,
                "battery_percent": payload.battery_percent,
            }
        },
        upsert=True
    )

    return {"status": "updated"}
