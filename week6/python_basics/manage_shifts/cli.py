from menu_base_model import MenuBaseModel
from data import Unit
from duty_manager import ManageDutiesMenu
from soldier_manager import ManageSoldiersMenu


class BaseMenu(MenuBaseModel):
    def __init__(self, unit: Unit) -> None:
        super().__init__(title="Base menu")
        self.unit = unit
        self.add_option(
            "s", "manage soldiers", lambda: ManageSoldiersMenu(self.unit).run()
        )
        self.add_option("d", "manage duties", lambda: ManageDutiesMenu(unit).run())
