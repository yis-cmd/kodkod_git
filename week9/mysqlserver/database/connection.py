from contextlib import contextmanager

from mysql.connector import connect

from config import config


@contextmanager
def get_cursor():
    conn = connect(
        host=config.host, port=config.port, user=config.user, password=config.password
    )
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()
