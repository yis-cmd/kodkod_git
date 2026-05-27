class Shape:
    def __init__(self, shape_id:str, shape_type:str):
        self.shape_id = shape_id
        self.shape_type = shape_type
    def get_area(self) -> float:
        ...
    def get_perimeter(self) -> float:
        ...
    def to_dict(self):
        return self.__dict__
    def __str__(self) -> str:
        return f"{self.__dict__}"