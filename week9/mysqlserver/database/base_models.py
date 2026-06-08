from pydantic import BaseModel, Field

class Constraint(BaseModel):
    type:str = Field(pattern=r"^(NOT NULL|UNIQUE|PRIMARY KEY|DEFAULT|AUTO_INCREMENT)( '[a-zA-Z0-9]+')?$")

    def __str__(self) -> str:
        return self.type

class Column(BaseModel):
    name:str = Field(pattern=r"^[a-zA-Z0-9_]+$")
    type:str = Field(pattern=r"^[a-zA-Z]+(\([0-9]+(,[0-9]+\))?)?$")
    constraints:list[Constraint] | None = None

class Columns(BaseModel):
    all:list[Column]