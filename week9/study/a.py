from fastapi import APIRouter

router = APIRouter(prefix="/users")
router_b = APIRouter(prefix="/prod")

@router.get("/")
def whatever(asdfgh:int):
    return

router_b.get("/")