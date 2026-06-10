from typing import Any, Sequence

from config import Config
from database.base_models import Column, Columns
from database.connection import DBConnection


def secure_identifiers(identifier: str) -> str:
    """
    takes an identifier and secures it against injections

    Args:
        identifier (str): the identifier

    Returns:
        identifier (str): the secured identifier
    """
    if not identifier.strip():
        raise ValueError("Identifiers cannot be empty or blank spaces")
    return f"`{identifier.replace("`", "``")}`"


def format_kv_pairs(
    data: dict[str, Any], join_with: str = " AND ", eq_sign: str = "="
) -> tuple[str, list[Any]]:
    clause_str = join_with.join(
        f"{secure_identifiers(name)} {eq_sign} %s" for name in data
    )
    return clause_str, list(data.values())


def format_filters(filters: dict[str, Any]) -> tuple[str, list[Any]]:
    return format_kv_pairs(filters, " AND ")


def format_updates(updates: dict[str, Any]) -> tuple[str, list[Any]]:
    return format_kv_pairs(updates, ", ")


def format_like_filter(filters: dict[str, Any]) -> tuple[str, list[Any]]:
    return format_kv_pairs(filters, " AND ", "LIKE")


class DBManager:
    def __init__(self, db_connection_config: Config) -> None:
        self.db_conn = DBConnection(db_connection_config)

    def create_db(self, name: str):
        stmt = f"CREATE DATABASE IF NOT EXISTS {secure_identifiers(name)}"
        self._execute(stmt)

    def drop_db(self, name: str):
        stmt = f"DROP DATABASE IF EXISTS {secure_identifiers(name)}"
        self._execute(stmt)

    def _execute(self, stmt: str):
        with self.db_conn as cur:
            cur.execute(f"{stmt};")

    def get_tables_manager(self, database: str):
        return TableManager(self.db_conn, database)


class TableManager:
    def __init__(self, conn: DBConnection, database: str) -> None:
        self.db_conn = conn
        self.database = database

    def _execute(self, stmt: str, values: Sequence | None = None):
        if not values:
            values = []
        with self.db_conn as cur:
            cur.execute(f"USE {secure_identifiers(self.database)};")
            return cur.execute(f"{stmt};", values)

    def create_table(self, table_name: str, columns: Columns):
        stmt = f"""
                CREATE TABLE IF NOT EXISTS {secure_identifiers(table_name)}(
                    {",\n".join(c.format_as_sql() for c in columns.all)}
                )
                """
        self._execute(stmt)

    def drop_table(self, table_name: str):
        stmt = f"DROP TABLE IF EXISTS {secure_identifiers(table_name)}"
        self._execute(stmt)

    def add_column(self, table_name: str, column: Column):
        stmt = f"ALTER TABLE {secure_identifiers(table_name)} ADD COLUMN {column.format_as_sql()}"
        self._execute(stmt)

    def rename_table(self, old_name: str, new_name: str):
        stmt = f"ALTER TABLE {secure_identifiers(old_name)} RENAME {secure_identifiers(new_name)}"
        self._execute(stmt)

    def rename_column(self, table_name: str, old_name: str, new_name: str):
        stmt = f"ALTER TABLE {secure_identifiers(table_name)} RENAME COLUMN {secure_identifiers(old_name)} TO {secure_identifiers(new_name)}"
        self._execute(stmt)

    def modify_column(self, table_name: str, column: Column):
        stmt = f"ALTER TABLE {secure_identifiers(table_name)} MODIFY {column.format_as_sql()}"
        self._execute(stmt)

    def drop_column(self, table_name: str, column_name: str):
        stmt = f"ALTER TABLE {secure_identifiers(table_name)} DROP COLUMN {secure_identifiers(column_name)}"
        self._execute(stmt)

    def insert(self, table_name, column_names: list[str], values: list[Any]):
        if len(column_names) != len(values):
            raise ValueError("Columns and values mismatch")
        place_holders = ",".join("%s" for _ in range(len(column_names)))
        stmt = f"INSERT INTO {secure_identifiers(table_name)} ({" ".join(secure_identifiers(i) for i in column_names)}) VALUES ({place_holders})"
        self._execute(stmt, values)

    def delete(self, table_name: str, filters: dict[str, str] | None = None):
        stmt = f"DELETE FROM {secure_identifiers(table_name)}"
        values = []
        if filters:
            filters_str, values = format_filters(filters)
            stmt += " WHERE " + filters_str
        self._execute(stmt, values)

    def update(
        self, table_name, update: dict[str, str], filters: dict[str, str] | None = None
    ):
        updates_str, values = format_updates(update)
        stmt = f"UPDATE {secure_identifiers(table_name)} SET {updates_str}"
        if filters:
            filters_str, filter_values = format_filters(filters)
            stmt += " WHERE " + filters_str
            values += filter_values
        self._execute(stmt, values)

    def _build_filters(
        self,
        filters: dict[str, Any] | None = None,
        like_filters: dict[str, str] | None = None,
    ) -> tuple[str, list[Any]]:
        where_clauses = []
        values = []
        if filters:
            filters_str, filters_values = format_filters(filters)
            where_clauses.append(filters_str)
            values += filters_values
        if like_filters:
            like_filters_str, like_filter_values = format_like_filter(like_filters)
            where_clauses.append(like_filters_str)
            values += like_filter_values
        return f"WHERE {" AND ".join(where_clauses)}", values

    def select(
        self,
        *,
        table_name: str,
        column_names: list[str],
        distinct: bool = False,
        ordered_by: list[str] | None = None,
        grouped_by: str | None = None,
        filters: dict[str, Any] | None = None,
        like_filters: dict[str, str] | None = None,
    ):
        secured_columns = ", ".join(secure_identifiers(c) for c in column_names)

        # base statement
        stmt: list[str] = []
        values: list[Any] = []
        stmt.append(
            f"SELECT {'DISTINCT ' if distinct else ""}{secured_columns} FROM {secure_identifiers(table_name)}"
        )

        # where clauses
        if filters or like_filters:
            where_clauses, filter_values = self._build_filters(filters, like_filters)
            stmt.append(where_clauses)
            values += filter_values

        # group by and order by clauses
        if grouped_by:
            stmt.append(f"GROUP BY {secure_identifiers(grouped_by)}")
        if ordered_by:
            stmt.append(
                f"ORDER BY {", ".join(secure_identifiers(o) for o in ordered_by)}"
            )

        # execute
        self._execute(" ".join(stmt), values)
