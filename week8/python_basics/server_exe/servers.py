from fastapi import FastAPI, HTTPException

app = FastAPI()

app.get("/numbers/{n}")
def is_positive(n):
    if n<0:
        raise HTTPException(400, "Number must be non-negative")
    return {"value": n}


students = {"101": "Moshe", "102": "Yosef"}
app.get("/students/{student_id}")
def get_student(student_id:str):
    student = students.get(student_id)
    if student:
        return student
    raise HTTPException(404)


app.post("/students/{student_id}")
def add_student(student_id:str, name:str):
    if student_id in students:
        raise HTTPException(409)
    students.update({student_id:name})

