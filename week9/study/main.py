from fastapi import FastAPI
from base_model import CreateUser, UpdateUser

app = FastAPI()

user: CreateUser


@app.post("/users/create")
def create_user(user_details: CreateUser):
    global user
    user = user_details
    print(user)

    user_dict = user.model_dump()
    print(user_dict)
    CreateUser.model_validate(user_dict)



@app.patch("/users/update")
def update_user(update_details: UpdateUser):
    global user
    update_dict = update_details.model_dump(exclude_none=True)
    user = user.model_copy(update=update_dict)
    print(user)