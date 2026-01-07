from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.users.models import UserCreate
from app.auth.service import hash_password, verify_password, get_user_by_email
from app.auth.jwt import create_access_token, decode_token
from app.core.database import db

router = APIRouter(prefix="/auth", tags=["Auth"])
security = HTTPBearer()


# ----------------------------
# SIGNUP
# ----------------------------
@router.post("/signup")
def signup(user: UserCreate):
    if user.role not in ["user", "admin"]:
        raise HTTPException(status_code=400, detail="Invalid role")

    if get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="User already exists")

    try:
        hashed_password = hash_password(user.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Insert user
    result = db.users.insert_one({
        "email": user.email,
        "password": hashed_password,
        "role": user.role
    })

    # ✅ CREATE JWT WITH user_id
    token = create_access_token(
        user_id=str(result.inserted_id),
        email=user.email
    )

    return {"access_token": token}


# ----------------------------
# LOGIN
# ----------------------------
@router.post("/login")
def login(email: str, password: str):
    user = get_user_by_email(email)

    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # ✅ CREATE JWT WITH user_id
    token = create_access_token(
        user_id=str(user["_id"]),
        email=user["email"]
    )

    return {"access_token": token}


# ----------------------------
# CURRENT USER
# ----------------------------
@router.get("/me")
def me(credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = decode_token(credentials.credentials)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = get_user_by_email(payload["email"])

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return {
        "email": user["email"],
        "role": user["role"],
        "user_id": str(user["_id"])
    }
