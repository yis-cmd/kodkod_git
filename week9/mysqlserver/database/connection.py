from typing import Sequence

from mysql.connector.abstracts import MySQLCursorAbstract
import mysql.connector

from config import Config


class DBConnection:
    def __init__(self, config: Config) -> None:
        self.config = config
        self._connection = None
        self._cursor:MySQLCursorAbstract | None = None

    def connect(self):
        self._connection = mysql.connector.connect(
            **self.config.model_dump(exclude_none=True)
        )
    
    def disconnect(self):
        if self._connection:
            self._connection.close()
            self._connection = None
    
    def commit(self):
        if self._connection and self._connection.is_connected():
            self._connection.commit()

    def rollback(self):
        if self._connection and self._connection.is_connected():
            self._connection.rollback()

    def execute(self, stmt:str, values:Sequence | None = None):
        if not values:
            values = []
        if not self._connection or not self._connection.is_connected():
            raise ConnectionError("No active database connection")
        self._cursor = self._connection.cursor()
        assert self._cursor
        self._cursor.execute(stmt, values)
        return self._cursor.fetchall()

    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.disconnect()
        return False
