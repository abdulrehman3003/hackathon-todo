from typing import Annotated
from uuid import UUID
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.auth.jwt import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user_id(token: Annotated[str, Depends(oauth2_scheme)]) -> UUID:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"detail": "Could not validate credentials", "code": "unauthorized"},
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = verify_token(token)
        user_id_str = payload.get("user_id")
        if user_id_str is None:
            raise credentials_exception
        user_id = UUID(user_id_str)
    except HTTPException:
        raise
    except Exception:
        raise credentials_exception
    return user_id
