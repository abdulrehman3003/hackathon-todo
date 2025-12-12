# Backend Project Structure (uv + FastAPI)

backend/
  pyproject.toml
  uv.lock
  .env.example
  README.md
  src/
    app/
      __init__.py
      main.py         # FastAPI app factory & app startup
      config.py       # Settings via pydantic-settings
      database/
        __init__.py
        connection.py # async DB pool
        migrations/
      models/
        __init__.py
        user.py
        task.py
      schemas/
        auth.py
        task.py
      auth/
        __init__.py
        jwt.py
        service.py
        routes.py
      tasks/
        __init__.py
        service.py
        routes.py
      tests/
        conftest.py
        test_auth.py
        test_tasks.py
