# pyproject.toml spec for uv-managed backend

[project]
name = "todo-backend"
version = "0.1.0"
description = "Hackathon II Todo Backend"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

Dependencies include (use uv add to install):
- fastapi
- uvicorn[standard]
- SQLModel or SQLAlchemy + databases/asyncpg
- asyncpg
- pydantic
- pydantic-settings
- python-dotenv
- passlib[bcrypt]
- python-jose[cryptography]
- alembic
- httpx (tests)
- pytest
- pytest-asyncio
Dev:
- ruff, mypy (optional), isort
Notes:
- Use `uv venv`, `uv add`, `uv lock` per constitution
