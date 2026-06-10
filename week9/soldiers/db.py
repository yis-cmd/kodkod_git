from contextlib import contextmanager

from mysql.connector import connect

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = "secret"
DATABASE = "soldiers_db"


@contextmanager
def get_connection():
    conn = connect(
        host="localhost",
        port=3306,
        user="root",
        password="secret",
        database="soldiers_db",
    )
    cur = conn.cursor(dictionary=True)
    try:
        yield cur
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


def get_schema():
    with get_connection() as cur:
        cur.execute("DESCRIBE soldiers;")
        rows = cur.fetchall()
        return [{"name": r["Field"], "type": r["Type"]} for r in rows]


def get_soldiers():
    with get_connection() as cur:
        cur.execute("SELECT * FROM soldiers")
        return cur.fetchall()
    
def get_soldier_by_id(soldier_id:int):
    with get_connection() as cur:
        cur.execute("SELECT * FROM soldiers WHERE id = %", (soldier_id,))

def 