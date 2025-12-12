from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.database.connection import get_session
from app.schemas.auth import UserRegister, UserLogin, UserResponse, Token
from app.auth.service import register_new_user, authenticate_user

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserRegister, session: Annotated[Session, Depends(get_session)]):
    return await register_new_user(user_data, session)

@router.post("/login", response_model=Token)
async def login(user_data: UserLogin, session: Annotated[Session, Depends(get_session)]):
    return await authenticate_user(user_data, session)
