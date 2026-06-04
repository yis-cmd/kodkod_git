from pydantic import BaseModel

class Weapon(BaseModel):
    id: int
    type: str
    model: str
    ammo_type: str
    condition: str

class WeaponNoID(BaseModel):
    type: str
    model: str
    ammo_type: str
    condition: str

class UpdateWeapon(BaseModel):
    type: str | None = None
    model: str | None = None
    ammo_type: str | None = None
    condition: str | None = None