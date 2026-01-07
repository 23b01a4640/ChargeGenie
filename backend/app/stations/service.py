from datetime import datetime
from bson import ObjectId
from app.core.database import db

def get_station_by_owner(owner_id: str):
    return db.stations.find_one({"owner_id": ObjectId(owner_id)})


def upsert_station(owner_id: str, data: dict):
    db.stations.update_one(
        {"owner_id": ObjectId(owner_id)},
        {
            "$set": {
                **data,
                "owner_id": ObjectId(owner_id),
                "updated_at": datetime.utcnow()
            }
        },
        upsert=True
    )
