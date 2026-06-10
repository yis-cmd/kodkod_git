from fastapi import FastAPI
from routers import greet

app = FastAPI()
app.include_router(greet.router)
