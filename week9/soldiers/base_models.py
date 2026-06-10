from pydantic import BaseModel

class BaseSoldier(BaseModel):
    name:str
    rank:str
    unit:str
    is_active:bool

class Soldier(BaseSoldier):
    id:int

class Create_soldier(BaseSoldier):
    pass

class UpdateSoldier():
    name:str | None = None
    rank:str | None = None
    unit:str | None = None
    is_active:bool | None = None
