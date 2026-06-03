from fastapi import APIRouter

router_a = APIRouter()


@router_a.get("/")
def get():
    return "noice"
