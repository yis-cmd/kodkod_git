class Student:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name


class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


class Thermometer:
    def __init__(self, celsius) -> None:
        self.celsius = celsius

    @property
    def celsius(self):
        return self.celsius

    @celsius.setter
    def celsius(self, degrees):
        if degrees < -273.15:
            raise ValueError
        self.celsius = degrees


class BankAccount:
    def __init__(self, balance) -> None:
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError
        self._balance -= amount


class Person:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Temperature:
    def __init__(self, celsius) -> None:
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, degrees):
        self.celsius = (degrees - 32) / (1.8)


class Calculator:
    @staticmethod 
    def is_even(n):
        return n % 2 == 0
    

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @classmethod 
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])

class User:
    counter = 0
    def __init__(self) -> None:
        self.counter += 1
    
    @classmethod
    def how_many(cls):
        return cls.counter
    

class Product:
    def __init__(self,name, price) -> None:
        self._name = name
        self._price = price
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        pass

    @price.setter
    def price(self,new_price):
        if new_price < 0:
            raise ValueError
        self._price = new_price