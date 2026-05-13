from collections.abc import Callable


class Task:
    def __init__(
        self, id: int, name: str, urgency_level: int, is_completed: bool
    ) -> None:
        self.id = id
        self.name = (name,)
        self.urgency_level = (urgency_level,)
        self.is_completed = is_completed

    def __str__(self) -> str:
        status = "completed" if self.is_completed else "pending"
        return f"name: {self.name}\nurgency level: {self.urgency_level}\nstatus: {status}\n"


class Tasks:
    tasks: list[Task] = []
    id = 1

    # pub
    def add_task(self):
        name = get_name()
        urgency_level = int(get_urgency_level())
        new_task = Task(self.id, name, urgency_level, False)
        self.id += 1
        self.tasks.append(new_task)

    def get_most_urgent_tasks(self):
        return [task for task in self.tasks if task.urgency_level == 1]

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.is_completed]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.is_completed]

    # pub
    def update_status(self):
        while True:
            id = int(get_number("Enter task id"))
            if id <= 0 or id > len(self.tasks):
                print("incorrect task id")
            else:
                break
        for task in self.tasks:
            if task.id == id:
                task.is_completed = True


def get_number(msg: str):
    while True:
        num = input(f"{msg}: ")
        if is_a_number(num):
            return num
        print("this was not a number try again")


def is_a_number(num: str):
    return num.isdigit()


def get_name():
    while True:
        name = input("Enter the task's name: ")
        if name:
            return name
        print("Name cannot be empty, try again")


def get_urgency_level():
    while True:
        urgency_level = get_number("Enter urgency level(1-3)")
        if is_valid_urgency_level(int(urgency_level)):
            return urgency_level
        print("this was not a valid choice try again")


def is_valid_urgency_level(urgency_level: int):
    return 3 >= urgency_level >= 1


# pub
def print_tasks(get_tasks: Callable[[], list[Task]]):
    tasks = get_tasks()
    for task in tasks:
        print(f"task number {task.id}")
        print(task)
        print()
    if not tasks:
        print("No taks found")


def unknown_choice():
    print("unknown choice")


# pub
def main():
    tasks = Tasks()
    choices = {
        1: tasks.add_task,
        2: lambda: print_tasks(tasks.get_pending_tasks),
        3: lambda: print_tasks(tasks.get_completed_tasks),
        4: tasks.update_status,
        5: lambda: print_tasks(tasks.get_most_urgent_tasks),
    }
    while True:
        show_menu()
        choice = int(get_number(""))
        if choice == 6:
            print("good bye")
            return
        choices.get(choice, unknown_choice)()


# pub
def show_menu():
    print("=== Task manager ===")
    print("1: add task")
    print("2: show pending tasks")
    print("3: show completed tasks")
    print("4: change task status")
    print("5: show urgent tasks")
    print("6: exit")


if __name__ == "__main__":
    main()
