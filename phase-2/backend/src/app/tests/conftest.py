import pytest
from httpx import AsyncClient
from sqlmodel import Session, SQLModel, create_engine
from app.config import settings
from app.main import app
from app.database.connection import get_session
import os

# Use a test database URL
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql://user:password@localhost:5432/test_db")
engine = create_engine(TEST_DATABASE_URL.replace("postgresql", "postgresql+asyncpg"))

@pytest.fixture(name="session")
async def session_fixture():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    async with Session(engine) as session:
        yield session
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

@pytest.fixture(name="client")
async def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
    app.dependency_overrides.clear()
