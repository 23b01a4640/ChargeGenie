from datetime import datetime
from bson import ObjectId
from app.core.database import db


def get_vehicle_profile(user_id: str):
    return db.vehicle_profiles.find_one(
        {"user_id": ObjectId(user_id)},
        {"_id": 0}
    )


def upsert_vehicle_profile(user_id: str, data: dict):
    db.vehicle_profiles.update_one(
        {"user_id": ObjectId(user_id)},
        {
            "$set": {
                "vehicle_range_km": data["vehicle_range_km"],
                "battery_percent": data["battery_percent"],
                "updated_at": datetime.utcnow(),
            }
        },
        upsert=True
    )
