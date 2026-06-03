from copy import deepcopy
from uuid import uuid4

from fastapi import HTTPException

from dependencies import DatabaseState
from soldier_modules import Soldier, SoldierNoID, UpdateSoldier
from logger_config import create_logger


logger = create_logger(__name__, "system.log")

def get_rank_from_id(soldier_id: str, data: DatabaseState):
    return soldier_lookup_by_id(soldier_id, data).rank


def soldier_lookup_by_id(soldier_id: str, data: DatabaseState):
    if soldier_id not in data.soldiers:
        logger.warning(f"soldier id {soldier_id} doesn't exist")
        raise HTTPException(404, f"soldier id {soldier_id} does not exist")
    return data.soldiers[soldier_id]


def add_soldier_logic(soldier_data: SoldierNoID, data: DatabaseState):
    soldier_dict = soldier_data.model_dump()
    new_id = str(uuid4())
    new_soldier = Soldier.model_validate({"id": new_id} | dict(**soldier_dict))
    return DatabaseState(deepcopy(data.soldiers) | {new_id: new_soldier}), new_id


def update_soldier_logic(
    old_soldier_data: Soldier, update_soldier_data: UpdateSoldier, data: DatabaseState
) -> DatabaseState:
    old_soldier_dict = old_soldier_data.model_dump()
    update_soldier_dict = update_soldier_data.model_dump(exclude_none=True)
    new_soldier_dict = old_soldier_dict | update_soldier_dict
    return DatabaseState(
        soldiers = deepcopy(data.soldiers)
        | {new_soldier_dict["id"]: Soldier.model_validate(new_soldier_dict)}
    )


def delete_soldier_logic(soldier_id: str, data: DatabaseState):
    new_data = deepcopy(data.soldiers)
    soldier = new_data.pop(soldier_id)
    return DatabaseState(new_data), soldier
