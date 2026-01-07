from datetime import datetime
from app.core.database import db
from bson import ObjectId

def create_history_entry(user_id: str, data: dict):
    record = {
        "user_id": ObjectId(user_id),
        **data,
        "chosen_at": datetime.utcnow()
    }
    db.charging_history.insert_one(record)


def get_user_history(user_id: str, limit: int = 10):
    return list(
        db.charging_history
        .find({"user_id": ObjectId(user_id)})
        .sort("chosen_at", -1)
        .limit(limit)
    )
