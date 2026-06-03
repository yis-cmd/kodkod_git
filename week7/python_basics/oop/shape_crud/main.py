from fastapi import FastAPI

from shape_manager import ShapeManager
from utils import get_int

from rectangle import Rectangle
from square import Square
from circle import Circle

app = FastAPI()
manager = ShapeManager()




@app.get("/")
def show():
    return "\n".join([str(shape) for shape in manager.get_all_shapes().values()])


@app.get("/{shape_id}")
def get_by_id():
    shape_id = get_int()
    shape = manager.get_shape_by_id(shape_id)
    return shape


@app.post("/add")
def add_shape(shape: Rectangle | Square | Circle):
    manager.create_shape(shape)


@app.patch("/update/{shape_id}")
def update_shape(shape_id:int, shape: Rectangle | Square | Circle):
    manager.update_shape(shape_id, shape)


@app.delete("/delete/{shape_id}")
def delete(shape_id):
    manager.delete_shape(shape_id)

