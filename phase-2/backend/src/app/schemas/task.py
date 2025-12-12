from typing import Optional, List
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field as PydanticField # Renamed Field to PydanticField to avoid conflict with SQLModel.Field

class TaskBase(BaseModel):
    title: str = PydanticField(min_length=1, max_length=200)
    description: Optional[str] = PydanticField(default=None, max_length=2000)

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    completed: Optional[bool] = None

class TaskResponse(TaskBase):
    id: int
    user_id: UUID
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True # Changed from orm_mode = True for Pydantic V2
        json_encoders = {
            datetime: lambda v: v.isoformat() + "Z", # Ensure ISO 8601 UTC format
        }

class TaskListResponse(BaseModel):
    data: List[TaskResponse]
    meta: dict # For pagination info

