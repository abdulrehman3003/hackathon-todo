# Backend Setup Fixes
Date: 2025-12-10

Summary:
- Corrected `pyproject.toml` parsing issues with `uv` by simplifying dependency declarations and removing unsupported sections (`[tool.uv.entry-points]`, `[project.scripts]` console commands).
- Updated `requires-python` in `pyproject.toml` from `>=3.9` to `>=3.10` to resolve Alembic dependency conflicts.
- Configured Alembic by initializing it and modifying `alembic.ini` and `env.py` to use `SQLModel.metadata` and load `.env` variables.
- Addressed `pydantic` validation error by changing `JWT_EXPIRES_IN` in `.env` and `.env.example` from "7d" to "604800" (seconds).

Notes:
- The initial Alembic migration generation is currently blocked due to a `ConnectionRefusedError`, indicating the PostgreSQL database is not running or accessible.
