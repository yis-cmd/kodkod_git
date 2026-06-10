from pydantic import BaseModel, Field
from datetime import datetime


class CreateUser(BaseModel):
    name: str = Field(min_length=5)
    age: int = Field(gt=17)
    created_at: datetime = Field(default_factory=datetime.now)


class UpdateUser(BaseModel):
    name: str | None = None
    age: int | None = None
    created_at: datetime | None = None


class User(BaseModel):
    id: int
    name: str
    age: int
    created_at: datetime = Field(default_factory=datetime.now)

