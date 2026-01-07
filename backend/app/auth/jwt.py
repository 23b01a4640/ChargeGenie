from jose import jwt, JWTError
from datetime import datetime, timedelta
import os

# ----------------------------
# Config
# ----------------------------

JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24


# ----------------------------
# Create JWT
# ----------------------------

def create_access_token(user_id: str, email: str):
    """
    Create JWT containing user_id and email.
    """
    payload = {
        "user_id": str(user_id),
        "email": email,
        "exp": datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)


# ----------------------------
# Decode JWT
# ----------------------------

def decode_token(token: str):
    """
    Decode and validate JWT.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
