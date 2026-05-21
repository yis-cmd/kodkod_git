from menu_base_model import MenuBaseModel
from data import Duty, Unit
import utils
import data
import exceptions
class BaseMenu(MenuBaseModel):
    def __init__(self, unit:Unit) -> None:
        super().__init__(title="Base menu")
        self.unit = unit
        self.add_option("s", "manage soldiers", lambda:ManageSoldiersMenu(self.unit).run())
        self.add_option("d", "manage duties", lambda:ManageDutiesMenu(unit).run())

class ManageSoldiersMenu(MenuBaseModel):
    def __init__(self, unit:Unit) -> None:
        super().__init__(title="Manage soldiers")
        self.unit = unit
        self.add_option("v", "view all soldiers", lambda:print(unit))
        self.add_option("a", "add soldier", self.add_soldier) 
        self.add_option("r", "remove soldier", self.remove_soldier) 
    
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

    def add_soldier(self):
        soldier_id = self.get_valid_new_id()
        name = utils.get_valid_name()
        soldier = data.Soldier(soldier_id, name)
        try:
            self.unit.add_soldier(soldier)
        except Exception as e:
            print(f"Unexpected error while adding: {e}")

    def remove_soldier(self):
        soldier_id = self.get_a_valid_ID()
        try:
            self.unit.remove_soldier(soldier_id)
        except Exception as e:
            print(f"Unexpected error happened while removing: {e}")

class ManageDutiesMenu(MenuBaseModel):
    def __init__(self, unit:Unit) -> None:
        super().__init__(title="Manage duties")
        self.unit = unit
        self.add_option("va", "view all duty types", lambda: print(unit.get_all_duty_types()))
        self.add_option("vs", "view duties for soldier", self.print_duties) 
        self.add_option("a", "add duty to soldier", self.add_duty_to_soldier)
        self.add_option("u", "update duty" ,self.update_duty) 
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
        while True:
            duty_name = utils.get_user_input()
            if duty_name in self.unit.duty_types:
                break
            print("Duty does not exist!, try again")
        duty_day = utils.get_valid_day()
        duty = Duty(duty_name, duty_day)
        try:
            self.unit.add_duty(soldier_id, duty)
        except Exception as e:
            print(f"Unexpected error occurred {e}")

    def update_duty(self):
        soldier_id = self.get_a_valid_ID()
        while True:
            duty_name = utils.get_user_input()
            if duty_name in self.unit.duty_types:
                break
            print("Duty does not exist!, try again")
        status = utils.get_valid_status()
        try:
            self.unit.update_duty_status(soldier_id, duty_name, status)
        except Exception as e:
             print(f"Unexpected error occurred {e}")