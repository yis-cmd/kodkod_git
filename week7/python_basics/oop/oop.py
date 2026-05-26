class Dog:
    def __init__(self, name: str) -> None:
        self.name = name

    def bark(self):
        return f"{self.name} says woof"


class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Counter:
    def __init__(self) -> None:
        self.counter = 0

    def increment(self):
        self.counter += 1

    def value(self):
        return self.counter


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class BankAccount:
    def __init__(self, balance=0) -> None:
        self.balance = balance

    def deposit(self, amount):
        # edge case about depositing a negative amount
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount


class Temperature:
    def __init__(self, celsius) -> None:
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32


class Student:
    school = "Kodkod"

    def __init__(self, name) -> None:
        self.name = name


a = Student("a")
b = Student("b")
b.name = "c"
assert a.name == "a"


class Player:
    counter = 0
    def __init__(self) -> None:
        self.counter += 1


class Money:
    def __init__(self, amount) -> None:
        self.amount = amount
    def is_more_than(self, other):
        return self.amount > other.amount
    
class Playlist:
    def __init__(self) -> None:
        self.titles = []
    def add(self, title):
        self.titles.append(title)
    def remove(self, title):
        self.titles.remove(title)
    def count(self):
        return len(self.titles)
    def __str__(self) -> str:
        return f"songs\n{"\n".join(self.titles)}"