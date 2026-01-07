from datetime import datetime
from bson import ObjectId
from app.core.database import db


def get_preferences(user_id: str):
    """
    Fetch preferences for a user.
    """
    return db.user_preferences.find_one(
        {"user_id": ObjectId(user_id)},
        {"_id": 0}
    )


def upsert_preferences(user_id: str, data: dict):
    """
    Create or update user preferences.
    """
    db.user_preferences.update_one(
        {"user_id": ObjectId(user_id)},
        {
            "$set": {
                "price_sensitivity": data["price_sensitivity"],
                "crowd_tolerance": data["crowd_tolerance"],
                "preferred_time": data["preferred_time"],
                "updated_at": datetime.utcnow(),
            }
        },
        upsert=True
    )
