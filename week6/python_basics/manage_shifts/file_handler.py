import json


def read(name:str) -> list:
    try:
        with open(name, "r") as file:
            if name.endswith("json"):
                return list(json.load(file))
            else:
                return list(file.read())
    except Exception:
        raise

def write(path:str, data):
    try:
        with open(path, "w") as file:
            if path.endswith("json"):
                json.dump(data, file)
            else:
                file.write(data)
    except Exception as e:
        raise

def append(path:str, data):
    try:
        with open(path, "a") as file:
            file.write(data)
    except Exception as e:
        raise