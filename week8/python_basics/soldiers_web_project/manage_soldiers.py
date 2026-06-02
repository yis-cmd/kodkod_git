from uuid import uuid4
from enum import Enum

from pydantic import BaseModel, ConfigDict
from utils.io import read, write
from fastapi import HTTPException


class Rank(Enum):
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5

class UpdateSoldier(BaseModel):
    name: str | None = None
    unit: str | None = None
    rank: str | None = None
    role: str | None = None
    is_active: str | None = None

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


class Soldiers:
    def __init__(self) -> None:
        self.filename = "soldiers.json"
        self.soldiers: dict[str, Soldier] = self.load_soldiers()

    def load_soldiers(self):
        data = read(self.filename)
        if not data:
            return {}
        soldiers = {s.get("id"): Soldier.model_validate(s) for s in data}
        return soldiers

    def commit(self):
        write(self.filename, [s.model_dump() for s in self.soldiers.values()])

    def get_all_soldiers(self):
        return [s.model_dump() for s in self.soldiers.values()]

    def get_soldier_by_id(self, soldier_id: str):
        soldier = self.soldiers.get(soldier_id)
        if soldier:
            return soldier
        raise HTTPException(404, "soldier does not exist")

    def add_soldier(self, soldier: SoldierNoID):
        new_id = str(uuid4())
        new_soldier = Soldier(
            id=new_id,
            name=soldier.name,
            unit=soldier.unit,
            rank=Rank(soldier.rank),
            role=soldier.role,
            is_active=soldier.is_active,
        )
        self.soldiers[new_id] = new_soldier
        self.commit()
        return new_id

    def update_soldier(self, soldier_id: str, **kwargs):
        soldier = self.soldiers.get(soldier_id)
        if not soldier:
            raise HTTPException(404, "soldier doesn't exist")
        soldier = soldier.model_dump()
        soldier.update(kwargs)
        self.soldiers[soldier_id] = Soldier.model_validate(soldier)
        self.commit()
        return 
        

    def delete_soldier(self, soldier_id: str):
        if soldier_id not in self.soldiers:
            raise HTTPException(404, "soldier not exists")
        soldier = self.soldiers.pop(soldier_id)
        self.commit()
        return soldier

    def get_rank_by_id(self, soldier_id: str):
        if soldier_id not in self.soldiers:
            raise HTTPException(404, "soldier not exists")
        return self.soldiers[soldier_id].rank
