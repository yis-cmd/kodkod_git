from abc import ABC

import exceptions
import utils
from low_data import DutyDto, Soldier, Duty


class SoldiersMng(ABC):
    def __init__(self) -> None:
        self.soldiers: dict[int, Soldier] = {}  # each entry is id : soldier
        self.duty_types: set[str] = set()

    def is_existing_id(self, soldier_id: int) -> bool:
        return soldier_id in self.soldiers

    def get_all_soldiers(self) -> list[Soldier]:
        return list(self.soldiers.values())

    def get_soldier_by_id(self, soldier_id: int) -> Soldier | None:
        return self.soldiers.get(soldier_id)

    def add_soldier(self, soldier_id: int, name: str) -> None:
        if self.is_existing_id(soldier_id):
            raise exceptions.DuplicateIDError
        soldier = Soldier(soldier_id, name)
        self.soldiers[soldier.id] = soldier

    def remove_soldier(self, soldier_id: int) -> Soldier:
        if not self.is_existing_id(soldier_id):
            raise exceptions.IDNotExistsError
        return self.soldiers.pop(soldier_id)


class Unit(SoldiersMng):
    def __str__(self) -> str:
        if not self.soldiers:
            return "no doldiers here yet"
        title = "==== Soldiers list ===="
        result = [
            f"{str(index)}. {str(soldier)}"
            for index, soldier in enumerate(self.soldiers.values(), start=1)
        ]
        result.insert(0, title)
        return "\n".join(result)

    def add_duty_type(self, duty_name):
        if duty_name in self.duty_types:
            raise exceptions.DutyTypeAlreadyExistsError
        self.duty_types.add(duty_name)

    def get_all_duty_types(self):
        return list(self.duty_types)

    def add_duty(self, soldier_id: int, duty_dto: DutyDto) -> None:
        if not self.is_existing_id(soldier_id):
            raise exceptions.IDNotExistsError
        if duty_dto.name not in self.duty_types:
            raise exceptions.DutyTypeNotExistsError
        if not utils.is_valid_day(duty_dto.day):
            raise exceptions.InvalidDayError
        duty = Duty(duty_dto.name.upper(), duty_dto.day)
        self.soldiers[soldier_id].add_duty(duty)

    def soldier_has_duty(self, soldier_id: int, duty_name: str) -> bool:
        if not self.is_existing_id(soldier_id):
            raise exceptions.IDNotExistsError
        if duty_name not in self.duty_types:
            raise exceptions.DutyTypeNotExistsError
        return self.soldiers[soldier_id].has_duty(duty_name)

    def update_duty_status(
        self, soldier_id: int, duty_name: str, new_status: str
    ) -> None:
        if not self.is_existing_id(soldier_id):
            raise exceptions.IDNotExistsError
        if not duty_name in self.duty_types:
            raise exceptions.DutyTypeNotExistsError
        self.soldiers[soldier_id].update_duty_status(duty_name, new_status)

    def get_soldier_duties(self, soldier_id: int) -> list[Duty]:
        if not self.is_existing_id(soldier_id):
            raise exceptions.IDNotExistsError
        return list(self.soldiers[soldier_id].duties.values())
