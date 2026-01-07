from pydantic import BaseModel
from typing import Optional

class StationInfo(BaseModel):
    place_id: str
    name: str
    lat: float
    lng: float

class RouteInfo(BaseModel):
    source: str
    destination: str
    distance_km: int

class VehicleInfo(BaseModel):
    range_km: int
    battery_percent: int

class ChargingHistoryCreate(BaseModel):
    station: StationInfo
    route: RouteInfo
    vehicle: VehicleInfo
    price_seen: Optional[int]
    crowd_status: Optional[str]
