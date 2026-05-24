from menu_base_model import MenuBaseModel
from data import Unit
import utils

class ManageSoldiersMenu(MenuBaseModel):
    def __init__(self, unit: Unit) -> None:
        super().__init__(title="Manage soldiers")
        self.unit = unit
        self.add_option("v", "view all soldiers", lambda: print(unit))
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
        try:
            self.unit.add_soldier(soldier_id, name)
        except Exception as e:
            print(f"Unexpected error while adding: {e}")

    def remove_soldier(self):
        soldier_id = self.get_a_valid_ID()
        try:
            self.unit.remove_soldier(soldier_id)
        except Exception as e:
            print(f"Unexpected error happened while removing: {e}")