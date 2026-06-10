from fastapi import APIRouter

router = APIRouter()

router.get("/hello/{name}")
def greetings(name:str):
    return  {"message": f"Hello,{name}"}