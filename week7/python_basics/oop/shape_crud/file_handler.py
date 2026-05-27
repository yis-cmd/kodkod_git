from json import JSONDecodeError, load, dump
import os
from pathlib import Path

def create_file(filename: str):
    if not Path(filename).exists():
        try:
            with open(filename, "x"):
                pass
        except Exception as e:
            raise FileNotFoundError(f"file couldn't be created due to exception {e}")


def read(filename: str) -> dict:
    if not Path(filename).exists():
        create_file(filename)
    with open(filename, "r") as file:
        try:
            data = load(file)
        except JSONDecodeError:
            data = {}
    return data 


def write(filename, data:dict[int,dict]) -> None:
    try:
        with open(filename, "w") as file:
            dump(data, file, indent=4)
    except Exception as e:
        raise FileNotFoundError(f"error writing {e}")