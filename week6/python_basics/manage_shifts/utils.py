import re
import exceptions

def get_valid_day() -> str:
    while True:
        print("Enter the day")
        day = get_user_input()
        if is_valid_day(day):
            return day
        print("This is an invalid day!, try again")


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


def get_valid_status():
    statuses = ["PENDING", "COMPLETED","MISSED"]
    while True:
        print("Enter the new status: ")
        response = get_user_input()
        if response.upper() in statuses:
            return response
        print("This is not a valid status")

def get_user_input() -> str:
    """
    gets non empty input from the user

    Returns:
        str: user input
    """
    while True:
        user_input = input()
        if user_input == "/q":
            raise exceptions.GoBack
        if is_not_empty_string(user_input):
            return user_input
        print("Empty input!, try again")


def is_not_empty_string(string: str) -> bool:
    return bool(string)


def get_positive_int_input() -> int:
    """
    gets input from the user forces int

    Returns:
        int: the input from the user as int
    """
    while True:
        number = get_user_input()
        if is_integer(number) and is_positive(int(number)):
            return int(number)
        print("This was not a number!, try again")


def is_integer(number: str) -> bool:
    try:
        int(number)
        return True
    except ValueError:
        return False


def is_positive(number: int) -> bool:
    return 0 <= number


def is_valid_name(name: str) -> bool:
    pattern = r"^[A-Za-z\s'-]{2,}$"
    return bool(re.match(pattern, name.strip()))


def get_user_choice(valid_choices: set) -> str:
    """
    מקבלת בחירה מהמשתמש.

    מקבלת: כלום

    מחזירה: מחרוזת המייצגת את בחירת המשתמש
    """
    while True:
        print("> ")
        choice = get_user_input()
        if choice in valid_choices:
            return choice
        print("Invalid choice!, try again")


def confirmation_menu(prompt:str = "are you sure you want to proceed? ") -> bool:
    """
    a way to ask the user to confirm weather he wants to proceed

    takes: prompt (str, optional)
    returns: bool
    """
    print(prompt)
    response = get_user_choice({"y","n"})
    return response == "y"

def get_valid_name() -> str:
    while True:
        print("Enter the soldier's name: ")
        response = get_user_input()
        if is_valid_name(response):
            return response
        print("This was not a valid name!, try again")
