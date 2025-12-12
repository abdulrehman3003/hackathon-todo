from typing import Optional, List
from datetime import datetime
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True, index=True)
    email: str = Field(unique=True, index=True, max_length=320)
    password_hash: str = Field(max_length=256) # Increased max_length
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    tasks: List["Task"] = Relationship(back_populates="user")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat() + "Z", # Ensure ISO 8601 UTC format
        }
