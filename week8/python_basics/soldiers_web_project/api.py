from fastapi import APIRouter, HTTPException

from utils.io import read_instructions
from dependencies import get_db, set_db, DatabaseState, commit_db
from soldier_modules import SoldierNoID, UpdateSoldier
import handle_data_logic
from logger_config import create_logger

MIN_RANK_TO_GET_SOLDIERS = 2
MIN_RANK_TO_ADD_SOLDIER = 3
MIN_RANK_TO_UPDATE_SOLDIER = 3
MIN_RANK_TO_DELETE_SOLDIER = 4

router = APIRouter()
logger = create_logger(__name__, "system.log")

def validate_requester(requester_id, required_rank, data: DatabaseState):
    if requester_id not in data.soldiers:
        logger.warning(f"{requester_id} tried to connect but this id does not exist")
        raise HTTPException(401, f"requester id {requester_id} does not exist")
    requester_rank = handle_data_logic.get_rank_from_id(requester_id, data)
    if requester_rank < required_rank:
        logger.warning(f"{requester_id} tried to do something he does not have authority to")
        raise HTTPException(
            403,
            f"requester {requester_id} doesn't have the required rank for this action",
        )

@router.get("/")
def home_page():
    return read_instructions()


@router.get("/soldiers")
def full_soldier_list(requester_id: str):
    logger.info(f"'{requester_id}' asked for full soldier list")
    data = get_db()
    validate_requester(requester_id, MIN_RANK_TO_GET_SOLDIERS, data)
    logger.info(f"'{requester_id}' got full soldier list")
    return [s.model_dump() for s in data.soldiers.values()]


@router.get("/soldiers/{soldier_id}")
def get_soldier_by_id(requester_id: str, soldier_id: str):
    logger.info(f"'{requester_id}' asked for '{soldier_id}' is detail")
    data = get_db()
    validate_requester(requester_id, MIN_RANK_TO_GET_SOLDIERS, data)
    logger.info(f"'{requester_id}' got '{soldier_id}' is detail")
    return handle_data_logic.soldier_lookup_by_id(soldier_id, data)


@router.post("/soldiers/add")
def add_soldier(requester_id: str, soldier_data: SoldierNoID):
    logger.info(f"'{requester_id}' asked to add {soldier_data}")
    data = get_db()
    validate_requester(requester_id, MIN_RANK_TO_ADD_SOLDIER, data)
    new_db, new_id = handle_data_logic.add_soldier_logic(soldier_data, data)
    set_db(new_db)
    commit_db()
    logger.info(f"'{requester_id}' added {soldier_data} with id '{soldier_data}'")
    return f"added soldier {soldier_data} with id {new_id}"


@router.patch("/soldiers/update/{soldier_id}")
def update_soldier(requester_id: str, soldier_id: str, updates: UpdateSoldier):
    logger.info(f"'{requester_id}' asked to update '{soldier_id}' with {updates}")
    data = get_db()
    validate_requester(requester_id, MIN_RANK_TO_UPDATE_SOLDIER, data)
    new_db = handle_data_logic.update_soldier_logic(
        handle_data_logic.soldier_lookup_by_id(soldier_id, data), updates, data
    )
    set_db(new_db)
    commit_db()
    logger.info(f"'{requester_id}' updated '{soldier_id}' with {updates}")
    return f"updated soldier {soldier_id} new details {new_db.soldiers[soldier_id]}"


@router.delete("/soldiers/delete/{soldier_id}")
def delete_soldier(requester_id: str, soldier_id: str):
    logger.info(f"'{requester_id}' asked to delete '{soldier_id}'")
    data = get_db()
    validate_requester(requester_id, MIN_RANK_TO_DELETE_SOLDIER, data)
    if soldier_id not in data.soldiers:
        raise HTTPException(404, f"soldier id {soldier_id} does not exist")
    new_db, soldier = handle_data_logic.delete_soldier_logic(soldier_id, data)
    set_db(new_db)
    commit_db()
    logger.info(f"'{requester_id}' deleted '{soldier}'")
    return f"deleted soldier {soldier_id}"
