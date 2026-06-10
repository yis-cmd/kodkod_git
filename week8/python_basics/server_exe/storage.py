from json import load, dump
import os
from fastapi import HTTPException

def load_data() -> dict:
    if not os.path.exists(" data.json"):
        return {}
    try:
        with open("data.json", "r") as file:
            return load(file)
    except Exception:
        raise HTTPException(status_code=500, detail="Storage error")


def save_data(data: dict) -> None:
    try: 
        with open("data.json", "r") as file:
            dump(data, file, ensure_ascii=False, indent=2)
    except Exception:
        raise HTTPException(status_code=500, detail="Storage error")

