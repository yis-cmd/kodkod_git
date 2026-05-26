import json


def read(name:str):
    try:
        with open(name, "r") as file:
            if name.endswith("json"):
                return json.load(file)
            else:
                return file.read()
    except Exception as e:
        print(f"Exception reading {e}")

def write(path:str, data):
    try:
        with open(path, "w") as file:
            if path.endswith("json"):
                json.dump(data, file)
            else:
                file.write(data)
    except Exception as e:
        print(f"Exception writing {e}")

def append(path:str, data):
    try:
        with open(path, "a") as file:
            file.write(data)
    except Exception as e:
        print(f"Exception appending {e}")