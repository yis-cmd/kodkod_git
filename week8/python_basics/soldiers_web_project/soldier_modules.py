from enum import IntEnum

from pydantic import BaseModel, ConfigDict


class Rank(IntEnum):
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5

class UpdateSoldier(BaseModel):
    name: str | None = None
    unit: str | None = None
    rank: Rank | None = None
    role: str | None = None
    is_active: bool | None = None

class SoldierNoID(BaseModel):
    name: str
    unit: str
    rank: Rank
    role: str
    is_active: bool


class Soldier(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    id: str
    name: str
    unit: str
    rank: Rank
    role: str
    is_active: bool
