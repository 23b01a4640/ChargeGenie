from passlib.context import CryptContext
from app.core.database import db

# Explicit bcrypt configuration (Windows-safe)
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=12
)

def hash_password(password: str):
    # bcrypt hard limit safety
    if len(password.encode("utf-8")) > 72:
        raise ValueError("Password too long (max 72 bytes)")
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)

def get_user_by_email(email: str):
    return db.users.find_one({"email": email})
