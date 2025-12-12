import pytest
from httpx import AsyncClient
from sqlmodel import Session, select
from app.models.user import User
from app.schemas.auth import UserResponse
import json

@pytest.mark.asyncio
async def test_register_success(client: AsyncClient):
    response = await client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "password123"}
    )
    assert response.status_code == 201
    user_data = UserResponse.model_validate(response.json())
    assert user_data.email == "test@example.com"
    assert user_data.id is not None
    assert user_data.created_at is not None

@pytest.mark.asyncio
async def test_register_duplicate_email(client: AsyncClient):
    await client.post(
        "/auth/register",
        json={"email": "duplicate@example.com", "password": "password123"}
    )
    response = await client.post(
        "/auth/register",
        json={"email": "duplicate@example.com", "password": "password123"}
    )
    assert response.status_code == 409
    assert response.json() == {"detail": "Email already registered", "code": "conflict"}

@pytest.mark.asyncio
async def test_login_success_returns_jwt(client: AsyncClient):
    await client.post(
        "/auth/register",
        json={"email": "login@example.com", "password": "password123"}
    )
    response = await client.post(
        "/auth/login",
        json={"email": "login@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
    assert response.json()["expires_in"] > 0

@pytest.mark.asyncio
async def test_login_bad_credentials(client: AsyncClient):
    response = await client.post(
        "/auth/login",
        json={"email": "nonexistent@example.com", "password": "wrongpassword"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect email or password", "code": "unauthorized"}

@pytest.mark.asyncio
async def test_register_invalid_password(client: AsyncClient):
    response = await client.post(
        "/auth/register",
        json={"email": "shortpass@example.com", "password": "short"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Password must be at least 8 characters", "code": "validation_error"}
