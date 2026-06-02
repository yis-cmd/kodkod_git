from json import dump, load
import os

__all__  = [
    "create_file",
    "read",
    "write"
]

def create_file(filename:str) -> None:
    """create a file

    Args:
        filename (str): the file name for creation

    Raises:
        FileNotFoundError: an unrecoverable error for the program when the file cannot be created
    """
    try:
        with open(filename, "w") as file:
            dump([], file)

    except Exception:
        raise FileNotFoundError("cannot create a file")

def read(filename:str):
    """read from json file

    Args:
        filename (str): the file name to read from
    
    Raises:
        JSONDecodeError: an unrecoverable error when the json is corrupted
        FileNotFoundError: an unrecoverable error for the program when the file cannot be created
        a number of other errors that makes it impossible to access the file
    """
    try:
        if not os.path.exists(filename):
            create_file(filename)
        with open(filename, "r") as file:
            return load(file)
    except Exception:
        raise IOError

def write(filename:str, data):
    """write to json file

    Args:
        filename (str): the file name to write to
    
    Raises:
        a number of errors that makes it impossible to access the file
    """
    try:
        with open(filename, "w") as file:
            dump(data, file, indent=2)
    except Exception:
        raise IOError
    
def read_instructions():
    with open("endpoint_chart.csv", "r") as file:
        titles = file.readline().strip().split(",")
        instructions = []
        for line in file:
            current = {title:curr for title, curr in zip(titles, line.strip().split(","))}
            instructions.append(current)
        return instructions

