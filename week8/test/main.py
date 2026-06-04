from fastapi import FastAPI, HTTPException

from app_io import read, write
from weapon_model import Weapon, WeaponNoID, UpdateWeapon

app = FastAPI()

FILENAME = "weapons.json"
VALID_CONDITIONS = ["new", "good", "damaged", "critical"]


def load_weapons():
    weapons: list[dict] = read(FILENAME)
    try:
        return {w["id"]: Weapon.model_validate(w) for w in weapons}
    except Exception as e:
        raise HTTPException(500, f"internal server error json file corrupted: {e}")


def export_weapons(weapons: dict[int, Weapon]):
    weapons_list = [w.model_dump() for w in weapons.values()]
    write(FILENAME, weapons_list)


@app.get("/weapons")
def get_all_weapons():
    return read(FILENAME)


@app.get("/weapons/by-condition")
def get_weapons_by_condition(condition: str):
    if condition not in VALID_CONDITIONS:
        raise HTTPException(422, "Invalid condition submitted")
    weapons = load_weapons()
    return [w.model_dump() for w in weapons.values() if w.condition == condition]


@app.get("/weapons/combat-ready")
def get_combat_ready_weapons(type):
    weapons = load_weapons()
    return [
        w.model_dump()
        for w in weapons.values()
        if w.type == type and w.condition in ["good", "new"]
    ]


@app.get("/weapons/summary/by-type")
def get_summary():
    weapons = load_weapons()
    summary: dict[str, int] = {}
    for w in weapons.values():
        if w.type in summary:
            summary[w.type] += 1
        else:
            summary[w.type] = 1
    return summary


@app.get("/weapons/{id}")
def get_weapon_by_id(id: int):
    weapons = load_weapons()
    if id not in weapons:
        raise HTTPException(404, "weapons id does not exist")
    return weapons[id]


@app.post("/weapons", status_code=201)
def add_weapon(weapon: WeaponNoID):
    if weapon.condition not in VALID_CONDITIONS:
        raise HTTPException(422, "Invalid condition submitted")
    weapons = load_weapons()
    new_id = max(weapons.keys()) + 1
    new_weapon_dict = weapon.model_dump()
    new_weapon_dict["id"] = new_id
    new_weapon_obj = Weapon.model_validate(new_weapon_dict)
    new_weapon_dict_list: dict[int, Weapon] = weapons | {new_id: new_weapon_obj}
    export_weapons(new_weapon_dict_list)
    return f"weapon {new_weapon_obj} created"


@app.put("/weapons/{id}")
def update_weapon(id: int, updates: UpdateWeapon):
    if updates.condition not in VALID_CONDITIONS and updates.condition is not None:
        raise HTTPException(422, "Invalid condition submitted")
    weapons = load_weapons()
    if id not in weapons:
        return HTTPException(404, "weapon id does not exist")
    updated_weapon = weapons[id].model_copy(
        update=updates.model_dump(exclude_none=True)
    )
    weapons[id] = updated_weapon
    export_weapons(weapons)
    return f"updated to {weapons[id]}"


@app.delete("/weapons/by-condition")
def delete_by_condition(condition:str):
    if condition not in VALID_CONDITIONS:
        raise HTTPException(422, "Invalid condition submitted")
    weapons = load_weapons()
    after_deletion = {w.id: w for w in weapons.values() if w.condition != condition}
    export_weapons(after_deletion)
    return f"deleted all weapons in {condition} condition"


@app.delete("/weapons/{id}")
def remove_weapon(id: int):
    weapons = load_weapons()
    if id not in weapons:
        return HTTPException(404, "weapon id does not exist")
    old_weapon = weapons.pop(id)
    export_weapons(weapons)
    return f"deleted {old_weapon}"


