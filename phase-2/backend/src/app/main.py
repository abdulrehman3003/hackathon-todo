from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database.connection import init_db
from app.auth.routes import router as auth_router
from app.tasks.routes import router as tasks_router
from app.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    # In a real app, you might want to run migrations here or ensure DB is up
    # For now, we'll just print a message
    print("Starting up...")
    # await init_db() # Uncomment for initial table creation if not using alembic immediately
    yield
    # Shutdown
    print("Shutting down...")

app = FastAPI(
    title="Todo App API",
    version="0.1.0",
    description="Backend API for Hackathon II Todo Application",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CORS_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception Handler for custom error format
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail,
    )

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}
