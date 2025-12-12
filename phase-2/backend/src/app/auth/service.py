from typing import Optional
from uuid import UUID
from fastapi import HTTPException, status
from sqlmodel import Session, select
from passlib.context import CryptContext

from app.models.user import User
from app.schemas.auth import UserRegister, UserLogin, UserResponse, Token
from app.auth.jwt import create_access_token, ACCESS_TOKEN_EXPIRE_SECONDS
from datetime import timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def register_new_user(user_data: UserRegister, session: Session) -> UserResponse:
    existing_user = session.exec(select(User).where(User.email == user_data.email)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"detail": "Email already registered", "code": "conflict"}
        )

    if len(user_data.password) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"detail": "Password must be at least 8 characters", "code": "validation_error"}
        )

    hashed_password = get_password_hash(user_data.password)
    new_user = User(email=user_data.email, password_hash=hashed_password)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return UserResponse(id=new_user.id, email=new_user.email, created_at=new_user.created_at)

async def authenticate_user(user_data: UserLogin, session: Session) -> Token:
    user = session.exec(select(User).where(User.email == user_data.email)).first()
    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"detail": "Incorrect email or password", "code": "unauthorized"}
        )
    
    access_token_expires = timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS)
    access_token = create_access_token(
        data={"sub": str(user.id), "email": user.email},
        expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer", expires_in=ACCESS_TOKEN_EXPIRE_SECONDS)

