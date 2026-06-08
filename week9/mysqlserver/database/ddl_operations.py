from database.base_models import Column, Columns
from table_manager_base import DBManager
from config import config

db_manager = DBManager(config)
college_mngr = db_manager.get_tables_manager("college")

def run_queries(query: str):
    college_mngr._execute(stmt=query)


def create_database():
    query = "CREATE DATABASE IF NOT EXISTS college;"
    run_queries(query)


def drop_database():
    query = "DROP DATABASE college;"
    run_queries(query)


def format_column(column: Column):
    formatted_column = f"`{column.name}` {column.type}"
    if column.constraints:
        constraints = " ".join(str(c) for c in column.constraints)
        formatted_column += " " + constraints
    return formatted_column


def create_table(table_name: str, columns: Columns):
    query = f"""
            CREATE TABLE IF NOT EXISTS `{table_name}` (
                {',\n'.join(format_column(column) for column in columns.all)}
            );
            """
    run_queries(query)


def add_phone_column():
    query = "ALTER TABLE students ADD COLUMN phone VARCHAR(20);"
    run_queries(query)


def add_birth_date_column():
    query = "ALTER TABLE students ADD COLUMN birth_date DATE;"
    run_queries(query)


def modify_email_column():
    query = "ALTER TABLE students MODIFY email VARCHAR(255);"
    run_queries(query)


def rename_courses_table():
    query = "ALTER TABLE courses RENAME TrainingCourses;"
    run_queries(query)


def drop_phone_column(column_name):
    query = f"ALTER TABLE students DROP COLUMN `{column_name}`;"
    run_queries(query)


def drop_teachers_table():
    query = f"DROP TABLE IF EXISTS teachers;"
    run_queries(query)


def drop_all_tables():
    query = "DROP TABLE IF EXISTS students; DROP TABLE IF EXISTS courses; DROP TABLE IF EXISTS teachers;"
    run_queries(query)
