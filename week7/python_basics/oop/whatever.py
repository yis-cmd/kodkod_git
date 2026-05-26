class Person:
    def __init__(self, name: str, age: int, net_worth: int) -> None:
        self.name = name
        self.age = age
        self.net_worth = net_worth

    def __eq__(self, value: object) -> bool:
        return self.net_worth == value
    
    def __lt__(self, other):
        return self.net_worth < other
    
    def __gt__(self, other):
        if isinstance(other, Person):
            return self.net_worth > other.net_worth
        else:
            return self.net_worth > other
    
    def __mul__(self, other):
        self.net_worth *= other

    def __truediv__(self, other):
        self.net_worth /= other

    def __sub__(self, other):
        self.net_worth -= other


yis = Person("yis", 23, 1001)
print(yis == 1000)
