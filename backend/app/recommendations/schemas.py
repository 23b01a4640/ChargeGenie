from pydantic import BaseModel
from typing import List, Optional


class StationInput(BaseModel):
    place_id: str
    lat: float
    lng: float
    distance_km: Optional[float] = None
    price_per_kwh: Optional[float] = 8
    availability: Optional[str] = "available"


class VehicleInput(BaseModel):
    range_km: float
    battery_percent: float


class RecommendationRequest(BaseModel):
    source: str
    destination: str
    stations: List[StationInput]
    vehicle: VehicleInput
