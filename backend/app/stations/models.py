from pydantic import BaseModel
from typing import Literal

class StationUpdate(BaseModel):
    price_per_kwh: int
    availability: Literal["available", "busy", "full"]
