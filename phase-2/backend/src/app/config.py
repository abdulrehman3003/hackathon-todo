from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_EXPIRES_IN: int = 604800 # 7 days
    CORS_ORIGIN: str = "http://localhost:5173"
    LOG_LEVEL: str = "info"

    # Optional for Uvicorn
    UV_PORT: int = 8000
    UV_HOST: str = "0.0.0.0"

    # Optional for DB pool
    DB_POOL_MIN: int = 1
    DB_POOL_MAX: int = 10

    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '.env'))

settings = Settings()
