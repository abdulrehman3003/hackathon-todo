from sqlmodel import SQLModel, create_engine
from typing import Generator
from app.config import settings

# In Alembic, we will use a different engine for migrations based on the sync/async needs.
# For application use, we define the async engine here.
engine = create_engine(settings.DATABASE_URL, echo=True,
                       pool_size=settings.DB_POOL_MIN, max_overflow=settings.DB_POOL_MAX-settings.DB_POOL_MIN)

async def init_db():
    # This function is primarily for creating tables in a non-migration context (e.g., tests or initial dev).
    # For production, Alembic migrations should be used.
    async with engine.begin() as conn:
        # SQLModel.metadata.create_all(conn.connection) # For synchronous engine
        await conn.run_sync(SQLModel.metadata.create_all) # For async engine

async def get_session() -> Generator:
    async with engine.begin() as session:
        try:
            yield session
        finally:
            await session.close()
