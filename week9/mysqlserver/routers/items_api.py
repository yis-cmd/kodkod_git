from fastapi import APIRouter

from database.base_models import Columns
from database.table_manager_base import DBManager
from config import config
from items_model import CreateItem, UpdateItem
from database.hardcoded_tables import tables
from create_logger import create_logger

db_manager = DBManager(config)
db_manager.create_db("store")
items_mngr = db_manager.get_tables_manager("store")

items_router = APIRouter()

logger = create_logger(__name__)

@items_router.post("/", status_code=201)
def create_setup():
    logger.info("POST /items/")
    setup = Columns(all=tables["items"])
    items_mngr.create_table("items", setup)
    return "setup created successfully"


@items_router.post("/add", status_code=201)
def add_item(new_item:CreateItem):
    logger.info("POST /items/add")
    items_mngr.insert_objects("items", new_item)
    item_id_column = items_mngr.get_max("items", "id")
    item_id = item_id_column[0]['MAX(`id`)'] #type: ignore
    return items_mngr.select(table_name="items", filters={"id":item_id})


@items_router.get("/")
def get_items():
    logger.info("GET /items/")
    return items_mngr.select(table_name="items")

@items_router.get("/{id}")
def get_item_by_id(id:int):
    logger.info(f"GET /items/{id}")
    return items_mngr.select(table_name="items", filters={"id":id})

@items_router.put("/{id}")
def update_item_by_id(id:int, update_item:UpdateItem):
    logger.info(f"PUT /items/{id} values {update_item}")
    items_mngr.update_with_object("items", update_item, filters={"id":id})
    return items_mngr.select(table_name="items", filters={"id":id})

@items_router.delete("/{id}")
def delete_item_by_id(id:int):
    logger.info(f"DELETE /items/{id}")
    item = items_mngr.select(table_name = "items", filters={"id":id})
    items_mngr.delete("items", filters={"id":id})
    return item