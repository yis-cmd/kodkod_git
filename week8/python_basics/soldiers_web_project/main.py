from fastapi import FastAPI, HTTPException, Response, status
import uvicorn

from utils.io import read_instructions
from logger_config import create_logger
from manage_soldiers import Soldiers, SoldierNoID, UpdateSoldier


app = FastAPI()
logger = create_logger(__name__, "system.log")
soldiers = Soldiers()

MIN_RANK_TO_GET_SOLDIERS = 2
MIN_RANK_TO_ADD_SOLDIER = 3
MIN_RANK_TO_UPDATE_SOLDIER = 3
MIN_RANK_TO_DELETE_SOLDIER = 4


@app.get("/")
def home_page():
    return read_instructions()

@app.get("/soldiers")
def get_all_soldiers(requester_id:str):
    logger.info(f"{requester_id} asking for full list of soldiers")
    try:
        requester_rank = soldiers.get_rank_by_id(requester_id)
        if requester_rank < MIN_RANK_TO_GET_SOLDIERS: #type: ignore
            logger.warning(f"{requester_id} requested list of all soldiers but is not authorized")
            return Response("requester is not authoraized for this data", status_code=status.HTTP_403_FORBIDDEN)
        logger.info(f"{requester_id} got all soldiers list")
        return soldiers.get_all_soldiers()
    except IOError:
        logger.critical("an io error while trying to fetch the list of soldiers")
        raise

    
@app.get("/soldiers/{soldier_id}")
def get_soldier_by_id(requester_id:str, soldier_id:str):
    logger.info(f"{requester_id} asking for soldier {soldier_id} is details")
    try:
        requester_rank = soldiers.get_rank_by_id(requester_id)
        if requester_rank < MIN_RANK_TO_GET_SOLDIERS: #type: ignore
            logger.warning(f"{requester_id} requested the details of soldier {soldier_id} but is not authorized")
            return Response("requester is not authoraized for this data", status_code=status.HTTP_403_FORBIDDEN)
        logger.info(f"{requester_id} got the details of {soldier_id}")
        return soldiers.get_soldier_by_id(soldier_id)
    except IOError:
        logger.critical("an io error while trying to fetch a soldier by id") 
        raise

@app.post("/soldiers/add")
def add_soldier(requester_id:str, soldier_data:SoldierNoID):
    logger.info(f"{requester_id} asking to add {soldier_data.model_dump()}")
    try:
        requester_rank = soldiers.get_rank_by_id(requester_id)
        if requester_rank < MIN_RANK_TO_ADD_SOLDIER: #type: ignore
            logger.warning(f"{requester_id} asked to add soldier {soldier_data.model_dump()} but the requester isn't authorized for that")
            raise HTTPException(403, "requester cannot add soldiers")
        soldier_id = soldiers.add_soldier(soldier_data)
        logger.info(f"{requester_id} added soldier {soldier_data.model_dump()} with id {soldier_id}")
        return Response(soldier_id, status.HTTP_201_CREATED)
    except IOError:
        logger.critical("an io error while trying to add a soldier") 
        raise

@app.patch("/soldiers/update/{soldier_id}")
def update_soldier(requester_id:str, soldier_id:str, updates:UpdateSoldier):
    logger.info(f"{requester_id} asking to update soldier {soldier_id} with {updates}")
    try:
        requester_rank = soldiers.get_rank_by_id(requester_id)
        if requester_rank < MIN_RANK_TO_UPDATE_SOLDIER: #type: ignore
            logger.warning(f"{requester_id} tried to update soldier {soldier_id} with {updates} but isn't authorized for it")
            return Response("requester cannot update soldiers", status_code=status.HTTP_403_FORBIDDEN)
        soldiers.update_soldier(soldier_id, **updates.model_dump(exclude_unset=True, exclude_defaults=True))
        logger.info(f"{requester_id} updated soldier {soldier_id} with {updates}")
        return "soldier updated successfully"
    except IOError:
        logger.critical("an io error while trying to update a soldier") 
        raise

@app.delete("/soldiers/delete/{soldier_id}")
def delete_soldier(requester_id:str, soldier_id:str):
    logger.info(f"{requester_id} asking to delete soldier {soldier_id}")
    try:
        requester_rank = soldiers.get_rank_by_id(requester_id)
        if requester_rank < MIN_RANK_TO_DELETE_SOLDIER: #type: ignore
            logger.warning(f"{requester_id} tried to delete {soldier_id} but doesn't have authorization for it")
            return Response("requester cannot delete a soldier", status_code=status.HTTP_403_FORBIDDEN)
        soldier = soldiers.delete_soldier(soldier_id)
        logger.info(f"{requester_id} deleted soldier {soldier_id}")
        return soldier.model_dump()
    except IOError:
        logger.critical("an io error while trying to delete a soldier")
        raise


if __name__ == "__main__":
    pass
