from pydantic import BaseModel, Field

class VehicleCreate(BaseModel):
    range_km: int = Field(..., gt=0)
    battery_percent: int = Field(..., ge=0, le=100)
