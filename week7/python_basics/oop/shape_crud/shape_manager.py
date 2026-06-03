from circle import Circle
from square import Square
from rectangle import Rectangle
from file_handler import read, write

FILENAME = "shapes.json"


class ShapeManager:
    def __init__(self):
        self.shapes: dict = {}
        self.load_from_json()

    def create_shape(self, shape):
        new_id = str(max((int(shape_id) for shape_id in self.shapes), default=-1) + 1)
        new_shape = {new_id: shape}
        self.shapes.update(new_shape)
        self.save_to_json()

    def get_all_shapes(self):
        return self.shapes

    def update_shape(self, shape_id, shape):
        self.shapes[shape_id] = shape
        

    def delete_shape(self, shape_id):
        self.shapes.pop(shape_id)

    def get_shape_by_id(self, shape_id):
        return self.shapes[str(shape_id)]

    def save_to_json(self):
        write(
            FILENAME, {shape.shape_id: shape.__dict__ for shape in self.shapes.values()}
        )

    def load_from_json(self):
        mapping = {"circle": Circle, "square": Square, "rectangle": Rectangle}
        shapes = read(FILENAME)
        for shape_id, shape in shapes.items():
            shape_cls = mapping.get(shape.get("shape_type"))
            assert shape_cls  # cuz i said so
            self.shapes.update({shape_id: shape_cls(**shape)})
