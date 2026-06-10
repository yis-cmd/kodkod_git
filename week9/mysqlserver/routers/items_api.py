from fastapi import APIRouter

from database.base_models import Columns
from database.table_manager_base import DBManager
from config import config
from items_model import CreateItem, UpdateItem
from database.hardcoded_tables import tables

db_manager = DBManager(config)
db_manager.create_db("store")
items_mngr = db_manager.get_tables_manager("store")

items_router = APIRouter()

@items_router.post("/", status_code=201)
def create_setup():
    setup = Columns(all=tables["items"])
    items_mngr.create_table("items", setup)
    return "setup created successfully"


@items_router.post("/add", status_code=201)
def add_item(new_item:CreateItem):
    items_mngr.insert_objects("items", new_item)
    item_id_column = items_mngr.select(table_name="items", column_names="MAX(id)")
    assert item_id_column is dict
    item_id = item_id_column['id']
    return items_mngr.select(table_name="items", filters={"id":item_id})


@items_router.get("/")
def get_items():
    return items_mngr.select(table_name="items")

@items_router.get("/items/{id}")
def get_item_by_id(id:int):
    return items_mngr.select(table_name="items", filters={"id":id})

@items_router.put("/items/{id}")
def update_item_by_id(id:int, update_item:UpdateItem):
    items_mngr.update_with_object("items", update_item, filters={"id":id})
    return items_mngr.select(table_name="items", filters={"id":id})

@items_router.delete("/{id}")
def delete_item_by_id(id:int):
    item = items_mngr.select(table_name = "items", filters={"id":id})
    items_mngr.delete("items", filters={"id":id})