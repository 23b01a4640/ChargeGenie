from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.auth.jwt import decode_token
from app.recommendations.schemas import RecommendationRequest
from app.recommendations.service import (
    shortlist_stations,
    generate_explanation
)

router = APIRouter(prefix="/recommend", tags=["Recommendation"])
security = HTTPBearer()


@router.post("/")
def recommend(
    payload: RecommendationRequest,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    decode_token(credentials.credentials)

    stations = [s.dict() for s in payload.stations]
    vehicle = payload.vehicle.dict()

    candidates = shortlist_stations(stations, vehicle)

    # ✅ REQUIRED fallback (you asked about this earlier)
    if not candidates:
        return {
            "top_5": stations[:5],
            "explanation": "Showing closest charging stations along your route."
        }

    explanation = generate_explanation(candidates, vehicle)

    return {
        "top_5": candidates,
        "explanation": explanation
    }
