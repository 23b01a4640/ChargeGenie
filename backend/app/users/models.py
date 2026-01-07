from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str  # "user" or "admin"

class UserPublic(BaseModel):
    email: EmailStr
    role: str
