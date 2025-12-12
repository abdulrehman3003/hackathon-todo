from typing import Optional
from pydantic import EmailStr, BaseModel
from datetime import datetime
from uuid import UUID

class UserRegister(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    created_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat() + "Z", # Ensure ISO 8601 UTC format
        }
