from fastapi import FastAPI
import setup
import db

app = FastAPI()

@app.post("/setup")
def make_setup():
    setup.create_soldiers_table()

@app.get("/schema")
def get_schema():
    return db.get_schema()

@app.get("/soldiers")
def get_soldiers():
    return {"soldiers": []}
