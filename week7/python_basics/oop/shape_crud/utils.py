def get_choice(valid_choices: list[str]) -> str:
    choice = input("> ")
    while not choice in valid_choices:
        print("Invalid choice!, try again")
        choice = input("> ")
    return choice


def get_int(msg:str | None = None) -> int:
    if msg:
        print(msg)
    shape_id = "1"
    while not isinstance(shape_id, int):
        try:
            shape_id = int(input())
        except (ValueError, TypeError):
            print("id must be a number!, try again")
    return shape_id
