# Todo Backend

This is the backend for the Hackathon II Todo application, built with FastAPI and `uv`.

## Setup

1.  **Install `uv`:**
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2.  **Create virtual environment and install dependencies:**
    ```bash
    cd backend
    uv venv
    uv pip install -e .
    ```

3.  **Configure Environment Variables:**
    Copy `.env.example` to `.env` and fill in your database URL and JWT secret.
    ```bash
    cp .env.example .env
    ```

4.  **Database Migrations:**
    Initialize and run Alembic migrations. (Detailed instructions will be provided in a separate spec/task)
    ```bash
    # alembic init -t async src/app/database/migrations
    # alembic revision --autogenerate -m "Initial migration"
    # alembic upgrade head
    ```

5.  **Run the application:**
    ```bash
    uv run start
    ```
    The API will be available at `http://localhost:8000`.

## Development

### Testing

```bash
uv run pytest -q
```

### Linting and Formatting

```bash
uv run ruff check .
uv run ruff format .
uv run isort .
```

### Database Seed (Optional)

(Instructions for seeding the database will be provided in a separate spec/task)
