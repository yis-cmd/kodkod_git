from contextlib import contextmanager
from mysql import connector

from base_models import Column


pool = [
    connector.connect(
        host="localhost",
        port=3306, 
        user="root", 
        password="secret", 
        database="mydb")
        for _ in range(10)
        ]

@contextmanager
def get_cursor():
    if not pool:
        raise Exception("Connection pool exhausted")
    conn = pool.pop()
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception:
        conn.rollback()
        raise 
    finally:
        cursor.close()
        pool.append(conn)


def safe_identifiers(identifier: str):
    identifier.replace("`", "``")
    return f"`{identifier}`"


def format_columns(columns: list[Column]) -> list[str]:
    table_columns: list[dict] = [c.model_dump() for c in columns]
    return [
        f"{safe_identifiers(c['name'])} {c['type']} {' '.join(c['constraints'])}".strip()
        for c in table_columns
    ]


def create_table(table_name: str, columns: list[Column]):
    if not columns:
        raise ValueError("No columns provided")
    with get_cursor() as cur:
        table_columns = ",\n".join(format_columns(columns))
        query = f"""
                CREATE TABLE IF NOT EXISTS {safe_identifiers(table_name)} (
                    {table_columns}
                );
                """
        query_2 = "CREATE DATABASE whatever;"
        print(query)
        cur.execute(query)


def select(**kwargs):
    with get_cursor() as cur:
            query = """
                        SELECT 
                        id, first_name, last_name, age, email
                        FROM 
                        students
                    """
            params = []
            if kwargs:
                params = list(kwargs.values())
                conditions = " AND ".join([f"{key} = %s" for key in kwargs])
                query += " WHERE " + conditions
            cur.execute(query, params=params)
            return cur.fetchall()
