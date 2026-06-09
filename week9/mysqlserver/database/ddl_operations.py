from database.base_models import Column
from database.table_manager_base import DBManager
from config import config

db_manager = DBManager(config)
college_mngr = db_manager.get_tables_manager("college")


def create_database():
    db_manager.create_db("college")


def drop_database():
    db_manager.drop_db("college")


def add_phone_column():
    college_mngr.add_column("students", Column(name="phone", type="VARCHAR(20)"))


def add_birth_date_column():
    college_mngr.add_column("students", Column(name="birth_date", type="DATE"))


def modify_email_column():
    college_mngr.modify_column("students", Column(name="email", type="VARCHAR(255)"))


def rename_courses_table():
    college_mngr.rename_table("courses", "TrainingCourses")


def drop_phone_column(column_name):
    college_mngr.drop_column("students", column_name)


def drop_teachers_table():
    college_mngr.drop_table("teachers")


def drop_all_tables():
    college_mngr.drop_table("students")
    college_mngr.drop_table("teachers")
    college_mngr.drop_table("courses")
