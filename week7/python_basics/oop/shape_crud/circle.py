from math import pi

from shape import Shape



class Circle(Shape):
    def __init__(self, shape_id:str, shape_type:str, radius):
        super().__init__(shape_id, shape_type)
        self.radius = radius

    def get_area(self) -> float:
        return self.radius ** 2 * pi
    
    def get_perimeter(self) -> float:
        return pi * (self.radius * 2)