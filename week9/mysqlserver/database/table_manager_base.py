from typing import Sequence

from config import Config
from database.base_models import Column, Columns
from database.connection import DBConnection


class DBManager:
    def __init__(self, db_connection_config:Config) -> None:
        self.db_conn = DBConnection(db_connection_config)

    def create_db(self, name:str):
        stmt = f"CREATE DATABASE `{name}`"
        self._execute(stmt)

    def drop_db(self, name:str):
        stmt = f"DROP DATABASE `{name}`"
        self._execute(stmt)

    def _execute(self, stmt:str):
        with self.db_conn as cur:
            cur.execute(f"{stmt};")

    def get_tables_manager(self, database:str):
        return TableManager(self.db_conn, database)


class TableManager:
    def __init__(self, conn:DBConnection, database:str) -> None:
        self.db_conn = conn
        self.database = database

    def _execute(self, stmt:str, values:Sequence | None = None):
        if not values:
            values = []
        with self.db_conn as cur:
            cur.execute(f"USE `{self.database}`;")
            cur.execute(f"{stmt};", values)

    def _fetch(self, stmt, values:Sequence | None = None):
        if not values:
            values = []
        with self.db_conn as cur:
            cur.execute(f"USE `{self.database}`;")
            cur.execute(f"{stmt};", values)
            return 

    def create_table(self, table_name:str, columns:Columns):
        stmt = f"""
                CREATE TABLE IF NOT EXISTS `{table_name}`(
                    {",\n".join(c.format_as_sql() for c in columns.all)}
                )
                """
        self._execute(stmt)   
    
    def drop_table(self, table_name:str):
        stmt = f"DROP TABLE IF EXISTS `{table_name}`"
        self._execute(stmt)

    def add_column(self, table_name:str, column:Column):
        stmt = f"ALTER TABLE `{table_name}` ADD COLUMN {column.format_as_sql()}"
        self._execute(stmt)
    
    def rename_table(self, old_name:str, new_name:str):
        stmt = f"ALTER TABLE `{old_name}` RENAME `{new_name}`"
        self._execute(stmt)

    def rename_column(self, table_name:str, old_name:str, new_name:str):
        stmt = f"ALTER TABLE `{table_name}` RENAME COLUMN `{old_name}` TO `{new_name}`"
        self._execute(stmt)
    
    def modify_column(self, table_name:str, column:Column):
        stmt = f"ALTER TABLE `{table_name}` MODIFY {column.format_as_sql()}"
        self._execute(stmt)

    def drop_column(self, table_name:str, column_name:str):
        stmt = f"ALTER TABLE `{table_name}` DROP COLUMN `{column_name}`"
        self._execute(stmt)
