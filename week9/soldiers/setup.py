from db import get_connection

def run_query(query:str):
    with get_connection() as cur:
        return cur.execute(query)

def create_soldiers_table():
    query = """
    CREATE TABLE IF NOT EXISTS soldiers (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        `rank` VARCHAR(50),
        unit VARCHAR(100),
        active BOOLEAN DEFAULT TRUE
    )
    """
    run_query(query)
    print("creation successful")
