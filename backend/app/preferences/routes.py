from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.auth.jwt import decode_token
from app.preferences.service import (
    get_preferences,
    upsert_preferences
)

router = APIRouter(prefix="/preferences", tags=["Preferences"])
security = HTTPBearer()


# ----------------------------
# Pydantic Schemas
# ----------------------------

class PreferencesRequest(BaseModel):
    price_sensitivity: str  # low | medium | high
    crowd_tolerance: str    # low | medium | high
    preferred_time: str     # morning | evening | night


# ----------------------------
# Helpers
# ----------------------------

def get_current_user_id(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    payload = decode_token(credentials.credentials)
    return payload["user_id"]


# ----------------------------
# Routes
# ----------------------------

@router.get("/me")
def fetch_my_preferences(user_id: str = Depends(get_current_user_id)):
    prefs = get_preferences(user_id)
    return prefs or {}


@router.put("/me")
def update_my_preferences(
    prefs: PreferencesRequest,
    user_id: str = Depends(get_current_user_id)
):
    if prefs.price_sensitivity not in ["low", "medium", "high"]:
        raise HTTPException(status_code=400, detail="Invalid price sensitivity")

    if prefs.crowd_tolerance not in ["low", "medium", "high"]:
        raise HTTPException(status_code=400, detail="Invalid crowd tolerance")

    if prefs.preferred_time not in ["morning", "evening", "night"]:
        raise HTTPException(status_code=400, detail="Invalid preferred time")

    upsert_preferences(user_id, prefs.dict())
    return {"message": "Preferences saved successfully"}
