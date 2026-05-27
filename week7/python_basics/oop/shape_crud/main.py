from shape_manager import ShapeManager
from utils import get_choice, get_int



def get_shape() -> str :
    shapes:dict[str, str] = {"1":"circle", "2":"square", "3":"rectangle"}
    menu = """
    === Shapes ===
    1. circle
    2. square
    3. rectangle
    """
    valid_choices = ['1', '2', '3']
    print(menu)
    choice = get_choice(valid_choices)
    return shapes[choice]

def get_params(shape:str) -> dict:
    match shape:
        case "circle":
            print("Enter the radius")
            radius = get_int()
            return  {"radius":radius}
        case "rectangle":
            print("Enter the length")
            length = get_int()
            print("enter the width")
            width = get_int()
            return {"height":length, "width":width}
        case "square":
            print("Enter the length")
            side = get_int()
            return {"side":side}
        case _:
            raise ValueError
        
            

def main() -> None :
    menu = """
    === Menu ===
    1. Add shape
    2. Show all shapes
    3. Update shape
    4. Delete shape
    5. Get shape by id
    6. Exit
    """
    manager = ShapeManager()
    running = True
    while running:
        valid_choices = ['1', '2', '3', '4', '5', '6']
        print(menu)
        choice = get_choice(valid_choices)

        match choice:
            case '1':
                print("0")
                shape = get_shape()
                print("1")
                parameters = get_params(shape)
                print("2")
                manager.create_shape(shape, **parameters)
                print("3")
            case '2':
                print("\n".join([str(shape) for shape in manager.get_all_shapes().values()]))
            case '3':
                shape_id = get_int("Enter the shape's id")
                shape_type = manager.get_shape_by_id(shape_id).shape_type
                params = get_params(shape_type)
                manager.update_shape(shape_id, shape_type = shape_type, **params)
            case '4':
                shape_id = get_int()
                manager.delete_shape(shape_id)
            case '5':
                shape_id = get_int()
                shape = manager.get_shape_by_id(shape_id)
                print(shape)
            case '6':
                running = False
            case _:
                raise ValueError



if __name__ == "__main__":
    main()