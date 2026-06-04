from json import load, dump
from fastapi import HTTPException

def read(filename:str):
    try:
        with open(filename, "r") as file:
            return load(file)
    except Exception as e:
        raise HTTPException(500, f"internal server error while reading the file:  {e}")

def write(filename, data):
    try:
        with open(filename, "w") as file:
            dump(data, file, indent=4)
    except Exception as e:
        raise HTTPException(500, f"internal server error while writing to the file: {e}")