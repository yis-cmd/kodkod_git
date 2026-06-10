from fastapi import FastAPI

from a import router, router_b

app = FastAPI()
app.include_router(router)
app.include_router(router_b)

app.get("/")
"/users/"