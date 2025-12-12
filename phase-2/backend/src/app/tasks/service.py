from typing import List, Optional
from uuid import UUID
from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse, TaskListResponse
from datetime import datetime

async def create_task_for_user(user_id: UUID, task_data: TaskCreate, session: Session) -> TaskResponse:
    new_task = Task(user_id=user_id, **task_data.model_dump())
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return TaskResponse.model_validate(new_task)

async def get_tasks_for_user(
    user_id: UUID,
    session: Session,
    status_filter: Optional[str] = "all",
    q: Optional[str] = None,
    limit: int = 20,
    offset: int = 0
) -> TaskListResponse:
    query = select(Task).where(Task.user_id == user_id)

    if status_filter == "pending":
        query = query.where(Task.completed == False)
    elif status_filter == "completed":
        query = query.where(Task.completed == True)

    if q:
        query = query.where(
            (Task.title.ilike(f"%{q}%")) | (Task.description.ilike(f"%{q}%"))
        )
    
    total_count_query = select(Task).where(Task.user_id == user_id)
    if status_filter != "all":
        total_count_query = total_count_query.where(Task.completed == (status_filter == "completed"))
    if q:
        total_count_query = total_count_query.where(
            (Task.title.ilike(f"%{q}%")) | (Task.description.ilike(f"%{q}%"))
        )
    total_count = (await session.exec(total_count_query)).count()

    query = query.offset(offset).limit(limit)
    tasks = (await session.exec(query)).all()

    return TaskListResponse(
        data=[TaskResponse.model_validate(task) for task in tasks],
        meta={"total": total_count, "limit": limit, "offset": offset}
    )

async def get_task_by_id_for_user(user_id: UUID, task_id: int, session: Session) -> TaskResponse:
    task = await session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"detail": "Task not found", "code": "not_found"})
    if task.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"detail": "Access denied", "code": "forbidden"})
    return TaskResponse.model_validate(task)

async def update_task_for_user(user_id: UUID, task_id: int, task_data: TaskUpdate, session: Session) -> TaskResponse:
    task = await session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"detail": "Task not found", "code": "not_found"})
    if task.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"detail": "Access denied", "code": "forbidden"})
    
    task_data_dict = task_data.model_dump(exclude_unset=True)
    task.sqlmodel_update(task_data_dict)
    task.updated_at = datetime.utcnow() # Manually update updated_at
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return TaskResponse.model_validate(task)

async def toggle_task_completion_for_user(user_id: UUID, task_id: int, session: Session) -> TaskResponse:
    task = await session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"detail": "Task not found", "code": "not_found"})
    if task.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"detail": "Access denied", "code": "forbidden"})
    
    task.completed = not task.completed
    task.updated_at = datetime.utcnow()
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return TaskResponse.model_validate(task)

async def delete_task_for_user(user_id: UUID, task_id: int, session: Session):
    task = await session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"detail": "Task not found", "code": "not_found"})
    if task.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"detail": "Access denied", "code": "forbidden"})
    
    await session.delete(task)
    await session.commit()
