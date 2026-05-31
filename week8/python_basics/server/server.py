import operator
import datetime

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/ping")
def pong():
    return {"status": "pong"}


@app.get("/greet/{name}")
def respond(name: str):
    return {"message": f"Hello, {name}!"}


#################################


@app.get("/")
def root():
    return {"service": "my-api", "version": "1.0"}


@app.get("/users/admin")
def get_user_admin():
    return {"role": "admin", "access": "full"}


#######################################


@app.get("/users/{user_id}")
def get_user(user_id):
    return {"user_id": user_id, "user_name": 6543, "user_email": "whatever@gmail.com"}


###################################
@app.get("/calc/{a}/{op}/{b}")
def calc(a: int, op: str, b: int):
    try:
        oper = getattr(operator, op)
        result = oper(a, b)
    except Exception:
        return f"operation {op} is not valid"
    return {"operation": op, "result": result}


###################################


@app.get("/status")
def status():
    return {"server name": "arbitrary name", "current time": datetime.datetime.now()}


###################################
grades = {
    "1": {"name": "Moshe", "grade": 88},
    "2": {"name": "Yaakov", "grade": 75},
    "3": {"name": "David", "grade": 92},
}


@app.get("/students")
def get_students():
    return grades


@app.get("/students/top")
def top_score():
    student_id, student_details = max(grades.items(), key=lambda x: x[1]["grade"])
    return {student_id: student_details}


@app.get("/students/average")
def get_avg():
    if len(grades) == 0:
        return 0
    return sum(details.get("grade", 0) for details in grades.values()) / len(grades)


@app.get("/students/count")
def student_count():
    return len(grades)


@app.get("/students/{student_id}")
def return_student_by_id(student_id: str):
    return grades.get(student_id)


###########################################3


def run():
    uvicorn.run(app="server:app", host="localhost", port=6543, reload=False)
