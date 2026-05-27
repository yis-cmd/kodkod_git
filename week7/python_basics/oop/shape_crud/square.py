from shape import Shape


class Square(Shape):
    def __init__(self, shape_id:str, shape_type:str, side):
        super().__init__(shape_id, shape_type)
        self.side = side

    def get_area(self) -> float:
        return self.side ** 2
    
    def get_perimeter(self) -> float:
        return self.side * 4