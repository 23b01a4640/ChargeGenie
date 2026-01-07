from fastapi import APIRouter
from app.maps.service import get_route, get_ev_stations_along_route

router = APIRouter(prefix="/maps", tags=["Maps"])

@router.post("/route")
def route(payload: dict):
    route_data = get_route(payload["source"], payload["destination"])
    stations = get_ev_stations_along_route(route_data["polyline"])

    return {
        "route": route_data,
        "stations": stations
    }
