from menu_base_model import MenuBaseModel
from data import Unit
import utils
from low_data import DutyDto
import exceptions

class ManageDutiesMenu(MenuBaseModel):
    def __init__(self, unit: Unit) -> None:
        super().__init__(title="Manage duties")
        self.unit = unit
        self.add_option(
            "va", "view all duty types", lambda: print(unit.get_all_duty_types())
        )
        self.add_option("vs", "view duties for soldier", self.print_duties)
        self.add_option("a", "add duty to soldier", self.add_duty_to_soldier)
        self.add_option("u", "update duty", self.update_duty)
        self.add_option("at", "add duty type", self.add_duty_type)

    def get_valid_new_id(self):
        while True:
            print("Enter the soldier's ID: ")
            response = utils.get_positive_int_input()
            if not self.unit.is_existing_id(response):
                return response
            print("ID already exists!, try again")

    def get_a_valid_ID(self):
        while True:
            print("Enter the soldier's ID: ")
            response = utils.get_positive_int_input()
            if self.unit.is_existing_id(response):
                return response
            print("ID does not exist!, try again")

    def add_duty_type(self):
        print("Enter the new type of duty")
        response = utils.get_user_input()
        try:
            self.unit.add_duty_type(response)
        except exceptions.DutyTypeAlreadyExistsError:
            print("Couldn't add duty type a duty with the same name already exists")

    def print_duties(self):
        response = self.get_a_valid_ID()
        try:
            soldier = self.unit.get_soldier_by_id(response)
            if not soldier:
                print("The soldier unexpectedly disappeared!")
                return
            print(f"==== {soldier} ====")
            for duty in soldier.duties.values():
                print(duty)
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

    def add_duty_to_soldier(self):
        soldier_id = self.get_a_valid_ID()
        print("Enter duty name")
        duty_name = utils.get_user_input()
        while not duty_name in self.unit.duty_types:
            print("Duty does not exist!, try again")
            print("Enter duty name")
            duty_name = utils.get_user_input()
        duty_day = utils.get_valid_day()
        duty = DutyDto(duty_name, duty_day)
        try:
            self.unit.add_duty(soldier_id, duty)
        except Exception as e:
            print(f"Unexpected error occurred {e}")

    def update_duty(self):
        soldier_id = self.get_a_valid_ID()
        print("Enter duty name ")
        duty_name = utils.get_user_input()
        while not duty_name in self.unit.duty_types:
            print("Duty does not exist!, try again")
            print("Enter duty name ")
            duty_name = utils.get_user_input()
        status = utils.get_valid_status()
        try:
            self.unit.update_duty_status(soldier_id, duty_name, status)
        except Exception as e:
            print(f"Unexpected error occurred {e}")