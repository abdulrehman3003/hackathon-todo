from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from app.config import settings
from fastapi import HTTPException, status
from app.schemas.auth import Token

SECRET_KEY = settings.JWT_SECRET
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECONDS = settings.JWT_EXPIRES_IN

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS)
    to_encode.update({"exp": expire, "iat": datetime.utcnow()})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        user_email: str = payload.get("email")
        if user_id is None or user_email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={"detail": "Could not validate credentials", "code": "unauthorized"},
                headers={"WWW-Authenticate": "Bearer"},
            )
        return {"user_id": user_id, "user_email": user_email}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"detail": "Could not validate credentials", "code": "unauthorized"},
            headers={"WWW-Authenticate": "Bearer"},
        )
