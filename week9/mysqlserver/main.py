from fastapi import FastAPI, HTTPException
from database import ddl_operations
from database.base_models import Columns
import database.hardcoded_tables

app = FastAPI()

@app.post("/tables/create")
def create_tables():
    try:
        for table_name, columns in database.hardcoded_tables.tables.items():
            ddl_operations.create_table(table_name, Columns.model_validate(columns))
        return {
                "success": True,
                "message": "All tables created successfully"
                }
    except Exception as error:
        raise HTTPException(500, {
                    "success": False,
                    "error": f"{error}"
                    })

@app.post("/tables/create/{table_name}")
def create_tables_dynamic(table_name:str, columns:Columns):
    try:
        ddl_operations.create_table(table_name, columns)
        return {
                "success": True,
                "message": f"table {table_name} created successfully"
                }
    except Exception as error:
        raise HTTPException(500, {
                    "success": False,
                    "error": f"{error}"
                    })

@app.put("/students/add-phone-column")
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

@app.delete("/tables")
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

@app.put("/students/add-birth-date")
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

@app.put("/students/modify-email")
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
    
@app.put("/courses/rename")
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

def main():
    pass

if __name__ == "__main__":
    main()
