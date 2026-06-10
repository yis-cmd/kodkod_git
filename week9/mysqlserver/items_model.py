from datetime import datetime

from pydantic import BaseModel, Field

class Item(BaseModel):
    id:int
    name:str = Field(max_length=100)
    description:str | None = None
    price:float = Field(ge=0.0)
    category:str = Field(max_length=50)
    is_active:bool = True
    created_at:datetime = Field(default_factory=datetime.now)

class CreateItem(BaseModel):
    name:str = Field(max_length=100)
    description:str | None = None
    price:float = Field(ge=0.0)
    category:str = Field(max_length=50)

class UpdateItem(BaseModel):
    name:str = Field(max_length=100)
    description:str | None = None
    price:float = Field(ge=0.0)
    category:str = Field(max_length=50)
    is_active:bool = True