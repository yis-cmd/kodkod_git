from shape import Shape


class Rectangle(Shape):
    def __init__(self, shape_id: str, shape_type: str, height, width):
        super().__init__(shape_id, shape_type)
        self.x = height
        self.y = width

    def get_area(self) -> float:
        return self.x * self.y

    def get_perimeter(self) -> float:
        return (self.x) * 2 + (self.y * 2)
    