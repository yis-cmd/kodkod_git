from pydantic import BaseModel


class Soldier(BaseModel):
    name: str
    phone: int


class UpdateSoldier(BaseModel):
    name: str | None = None
    phone: int | None = None

a = Soldier(name = "s", phone = 1)
u = UpdateSoldier(name = "t")

print(a)

dict_a = a.model_dump()
dict_u = u.model_dump(exclude_none=True)

new_dict = dict_a | dict_u

a = Soldier.model_validate(new_dict)
print(a)