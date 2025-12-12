from typing import Annotated, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, Query, status
from app.database.connection import get_session
from sqlmodel import Session

from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse, TaskListResponse
from app.tasks.service import (
    create_task_for_user,
    get_tasks_for_user,
    get_task_by_id_for_user,
    update_task_for_user,
    toggle_task_completion_for_user,
    delete_task_for_user
)
from app.auth.dependencies import get_current_user_id # Assuming this dependency exists

router = APIRouter()

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreate,
    current_user_id: Annotated[UUID, Depends(get_current_user_id)],
    session: Annotated[Session, Depends(get_session)]
):
    return await create_task_for_user(current_user_id, task_data, session)

@router.get("/", response_model=TaskListResponse)
async def list_tasks(
    current_user_id: Annotated[UUID, Depends(get_current_user_id)],
    session: Annotated[Session, Depends(get_session)],
    status: Optional[str] = Query("all", pattern="^(all|pending|completed)$"),
    q: Optional[str] = Query(None),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    return await get_tasks_for_user(current_user_id, session, status, q, limit, offset)

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    current_user_id: Annotated[UUID, Depends(get_current_user_id)],
    session: Annotated[Session, Depends(get_session)]
):
    return await get_task_by_id_for_user(current_user_id, task_id, session)

@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task_data: TaskUpdate,
    current_user_id: Annotated[UUID, Depends(get_current_user_id)],
    session: Annotated[Session, Depends(get_session)]
):
    return await update_task_for_user(current_user_id, task_id, task_data, session)

@router.patch("/{task_id}/toggle", response_model=TaskResponse)
async def toggle_task_completion(
    task_id: int,
    current_user_id: Annotated[UUID, Depends(get_current_user_id)],
    session: Annotated[Session, Depends(get_session)]
):
    return await toggle_task_completion_for_user(current_user_id, task_id, session)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    current_user_id: Annotated[UUID, Depends(get_current_user_id)],
    session: Annotated[Session, Depends(get_session)]
):
    await delete_task_for_user(current_user_id, task_id, session)
    return
