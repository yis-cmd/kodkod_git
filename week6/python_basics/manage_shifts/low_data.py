from dataclasses import dataclass, field
from enum import StrEnum
import exceptions


class DutyStatus(StrEnum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    MISSED = "MISSED"


@dataclass
class DutyDto:
    name: str
    day: str


@dataclass
class Duty:
    name: str
    day: str
    status: DutyStatus = DutyStatus.PENDING

    def __str__(self) -> str:
        return f"{self.name}, {self.day}, {self.status}"


@dataclass
class Soldier:
    id: int
    name: str
    # each entry is name : duty object
    duties: dict[str, Duty] = field(default_factory=dict)

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}"

    def add_duty(self, duty: Duty):
        if duty.name in self.duties:
            raise exceptions.DuplicatedDutiesForIDError
        self.duties[duty.name] = duty

    def update_duty_status(self, duty_name: str, new_status: str):
        if duty_name not in self.duties:
            raise exceptions.DutyNotExistsForIDError
        self.duties[duty_name].status = DutyStatus(new_status.upper())

    def has_duty(self, duty_name: str):
        return duty_name in self.duties

    def get_duties(self):
        return list(self.duties.values())
