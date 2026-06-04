from json import load, dump
from fastapi import HTTPException

from set_logger import create_logger

logger = create_logger(__name__)

def read(filename:str):
    try:
        with open(filename, "r") as file:
            return load(file)
    except Exception as e:
        logger.exception("error while reading from file")
        raise HTTPException(500, f"internal server error while reading the file:  {e}")

def write(filename, data):
    try:
        with open(filename, "w") as file:
            dump(data, file, indent=4)
    except Exception as e:
        logger.exception("error while writing to file")
        raise HTTPException(500, f"internal server error while writing to the file: {e}")