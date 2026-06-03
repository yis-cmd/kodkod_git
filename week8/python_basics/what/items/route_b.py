from fastapi import APIRouter

router_b = APIRouter()

@router_b.get("/a")
def get():
    return {'a':"a"}
