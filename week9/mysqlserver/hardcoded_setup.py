from fastapi import APIRouter, HTTPException

import database.hardcoded_tables
from database.base_models import Columns
from database import ddl_operations
from database.table_manager_base import DBManager

from config import config

router = APIRouter()
db_manager = DBManager(config)
college_mngr = db_manager.get_tables_manager("college")


@router.post("/tables/create")
def create_tables():
    try:
        for table_name, columns in database.hardcoded_tables.tables.items():
            college_mngr.create_table(table_name, Columns(all=columns))
        return {
                "success": True,
                "message": "All tables created successfully"
                }
    except Exception as error:
        raise HTTPException(500, {
                    "success": False,
                    "error": f"{error}"
                    })
    
@router.put("/students/add-phone-column")
def patch_table():
    try:
        ddl_operations.add_phone_column()
        return {
                "success": True,
                "message": "Phone column added successfully"
                }
    except Exception as error:
        raise HTTPException(500, {
                    "success": False,
                    "error": f"{error}"
                    })

@router.delete("/tables")
def drop_tables():
    try:
        ddl_operations.drop_all_tables()
        return {
                "success": True,
                "message": "All tables deleted successfully"
                }
    except Exception as error:
        raise HTTPException(500, {
                    "success": False,
                    "error": f"{error}"
                    })

@router.put("/students/add-birth-date")
def add_bd_date():
    try:
        ddl_operations.add_birth_date_column()
        return {
            "success": True,
            "message": "birth day date column added"
        }
    except Exception as error:
        raise HTTPException(500, {
                    "success": False,
                    "error": f"{error}"
                    })

@router.put("/students/modify-email")
def modify_email_column():
    try:
        ddl_operations.modify_email_column()
        return {
            "success": True,
            "message": "birth day date column added"
        }
    except Exception as error:
        raise HTTPException(500, {
                    "success": False,
                    "error": f"{error}"
                    })
    
@router.put("/courses/rename")
def rename_column():
    try:
        ddl_operations.rename_courses_table()
        return {
            "success": True,
            "message": "birth day date column added"
        }
    except Exception as error:
        raise HTTPException(500, {
                    "success": False,
                    "error": f"{error}"
                    })