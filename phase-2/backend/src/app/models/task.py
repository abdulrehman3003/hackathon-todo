from typing import Optional
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=2000)
    completed: bool = Field(default=False, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    user_id: UUID = Field(foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="tasks")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat() + "Z", # Ensure ISO 8601 UTC format
        }
