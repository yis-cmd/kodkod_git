from fastapi import FastAPI

from database.base_models import Column, Columns
from database.table_manager_base import DBManager

from config import config
import hardcoded_setup
from routers.items_api import items_router

app = FastAPI()
app.include_router(hardcoded_setup.router)
app.include_router(items_router, prefix="/items")

db_manager = DBManager(config)
college_mngr = db_manager.get_tables_manager("college")


@app.post("/tables/create/{table_name}")
def create_tables(table_name: str, columns: Columns):
    college_mngr.create_table(table_name, columns)


@app.delete("/table/drop/{table_name}")
def delete_table(table_name: str):
    college_mngr.drop_table(table_name)


@app.put("/tables/add_column/{table_name}")
def add_column(table_name: str, column: Column):
    college_mngr.add_column(table_name, column)


@app.patch("/tables/modify_column/{table_name}")
def modify_column(table_name: str, column: Column):
    college_mngr.modify_column(table_name, column)


@app.patch("/tables/rename_table/{table_name}")
def table_rename(table_name: str, new_name: str):
    college_mngr.rename_table(table_name, new_name)


@app.patch("/tables/rename_column/{table_name}/{column_name}")
def column_rename(table_name: str, column_name: str, new_name: str):
    college_mngr.rename_column(table_name, column_name, new_name)
