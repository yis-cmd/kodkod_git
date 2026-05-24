import re

import custom_exceptions
from low_data import DutyStatus


def is_not_empty_string(string: str) -> bool:
    return bool(string)


def get_user_input(msg: str | None = None) -> str:
    """
    gets non empty input from the user

    Returns:
        str: user input
    """
    if msg:
        print(msg)
    user_input = input()
    while user_input == "":
        user_input = input()
        if user_input == "exit":
            raise custom_exceptions.GoBack
        print("Empty input!, try again")
    return user_input


def is_valid_day(day: str) -> bool:
    """
    checks if the day is valid
    takes: day as str
    returns: bool
    """
    days = {
        "sunday": True,
        "monday": True,
        "tuesday": True,
        "wednesday": True,
        "thursday": True,
        "friday": False,
        "saturday": False,
    }
    return days.get(day, False)


def get_valid_day() -> str:
    print("Enter the day")
    day = get_user_input()
    while not is_valid_day(day):
        print("Enter the day")
        day = get_user_input()
        print("This is an invalid day!, try again")
    return day


def is_valid_status(status: str) -> bool:
    return status.upper() in DutyStatus


def get_valid_status():
    print("Enter the new status: ")
    response = get_user_input()
    while not is_valid_status(response):
        print("Enter the new status: ")
        response = get_user_input()
        print("This is not a valid status")
    return response


def is_integer(number: str) -> bool:
    try:
        int(number)
        return True
    except ValueError:
        return False


def is_positive(number: int) -> bool:
    return 0 <= number


def get_positive_int_input() -> int:
    """
    gets input from the user forces int

    Returns:
        int: the input from the user as int
    """
    number = get_user_input()
    while not (is_integer(number) and is_positive(int(number))):
        number = get_user_input()
        print("This was not a number!, try again")
    return int(number)


def is_valid_name(name: str) -> bool:
    pattern = r"^[A-Za-z\s'-]{2,}$"
    return bool(re.match(pattern, name.strip()))


def get_valid_name() -> str:
    print("Enter the soldier's name: ")
    response = get_user_input()
    while not is_valid_name(response):
        print("Enter the soldier's name: ")
        response = get_user_input()
        print("This was not a valid name!, try again")
    return response


def get_user_choice(valid_choices: set) -> str:
    """
    מקבלת בחירה מהמשתמש.

    מקבלת: כלום

    מחזירה: מחרוזת המייצגת את בחירת המשתמש
    """
    print("> ", end="")
    choice = get_user_input()
    while choice not in valid_choices:
        print("> ", end="")
        choice = get_user_input()
        print("Invalid choice!, try again")
    return choice


def confirmation_menu(prompt: str = "are you sure you want to proceed? ") -> bool:
    """
    a way to ask the user to confirm weather he wants to proceed

    takes: prompt (str, optional)
    returns: bool
    """
    print(prompt)
    response = get_user_choice({"y", "n"})
    return response == "y"
