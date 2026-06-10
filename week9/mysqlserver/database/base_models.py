from pydantic import BaseModel, Field

class Constraint(BaseModel):
    type:str = Field(pattern=r"^(NOT NULL|UNIQUE|PRIMARY KEY|DEFAULT|AUTO_INCREMENT)( '[a-zA-Z0-9_]+')?$")

    def format_as_sql(self) -> str:
        return self.type

class Column(BaseModel):
    name:str = Field(pattern=r"^[a-zA-Z0-9_]+$")
    type:str = Field(pattern=r"^[a-zA-Z]+(\([0-9]+(,[0-9]+)?\))?$")
    constraints:list[Constraint] | None = None

    def format_as_sql(self):
        formatted_column = f"`{self.name}` {self.type}"
        if self.constraints:
            constraints = " ".join(c.format_as_sql() for c in self.constraints)
            formatted_column += " " + constraints
        return formatted_column

class Columns(BaseModel):
    all:list[Column]