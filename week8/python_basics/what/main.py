from fastapi import FastAPI
from items import route, route_b

app = FastAPI()

app.include_router(route.router_a)
app.include_router(route_b.router_b)