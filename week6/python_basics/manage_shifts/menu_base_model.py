from abc import ABC
from collections.abc import Callable

import custom_exceptions
import utils


class MenuBaseModel(ABC):  # ABC doesn't force anything just a declaration of intent
    def __init__(self, title) -> None:
        self.title: str = title
        self.options: dict[str, tuple[str, Callable]] = {}
        self.add_option("exit", "Go back", self.go_back)

    def add_option(self, key: str, description: str, action: Callable):
        """
        add an option to the menu

        Args:
            key (str): what will be the key to type in order to run the action
            description (str): description of the action
            action (Callable): the function to activate for the choice
        """
        self.options[key] = (description, action)

    def show_options(self) -> None:
        """
        format and show menu for the menu
        takes: nothing
        returns: nothing
        """
        print(f"==== {self.title} ====")
        for key, (description, _) in self.options.items():
            if key == "Default":  # Default should be reserved for error handling
                continue
            print(f"{key}. {description}")
        print("> ", end="")

    def go_back(self):
        raise custom_exceptions.GoBack()

    def run(self):
        is_running = True
        while is_running:
            try:
                self.show_options()
                # the user should not be allowed to trigger error handling like that
                choice = utils.get_user_choice(
                    {k for k in self.options if k != "Default"}
                )
                fallback = ("Invalid", lambda: print("Invalid key!, try again"))
                self.options.get(choice, self.options.get("Default", fallback))[1]()
            except custom_exceptions.GoBack:
                is_running = False
