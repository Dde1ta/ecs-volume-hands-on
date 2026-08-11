import socket

from fastapi import FastAPI, HTTPException
from models import Student, Teacher, Course
from data_interface import Data

app = FastAPI()
data = Data()


@app.get("/")
def health_check():
    return {"message": "API healthy and ready"}


@app.get("/who")
def whoami():
    container_id = socket.gethostname()
    return {"message": "Successful !!", "result": {
        "container_id": container_id
    }}


@app.get("/student/all")
def get_all_students():
    students = data.get_all(Student)
    return {"message": "Successful !!", "result": students}


@app.get("/teacher/all")
def get_all_teachers():
    teachers = data.get_all(Teacher)
    return {"message": "Successful !!", "result": teachers}


@app.get("/course/all")
def get_all_course():
    courses = data.get_all(Course)
    return {"message": "Successful !!", "result": courses}


@app.get("/student/{_id}")
def get_student(_id: int):
    try:
        student = data.get_id(Student, _id)
        return {"message": "Successful !!", "result": student}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/teacher/{_id}")
def get_teacher(_id: int):
    try:
        teacher = data.get_id(Teacher, _id)
        return {"message": "Successful !!", "result": teacher}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/course/{_id}")
def get_course(_id: int):
    try:
        course = data.get_id(Course, _id)
        return {"message": "Successful !!", "result": course}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post("/student/new")
def add_new_student(student: Student):
    try:
        data.add(student)
        return {"message": "Successful !!", "result": "student added :D"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/teacher/new")
def add_new_teacher(teacher: Teacher):
    try:
        data.add(teacher)
        return {"message": "Successful !!", "result": "teacher added :D"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/course/new")
def add_new_course(course: Course):
    try:
        data.add(course)
        return {"message": "Successful !!", "result": "course added :D"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.patch("/student/update/{_id}")
def update_student(student: Student, _id: int):
    status = data.update_id(student, _id)
    if status:
        return {"message": "Successful !!", "result": "student updated :D"}
    else:
        raise HTTPException(status_code=404, detail=f"student with id {_id} not found")


@app.patch("/teacher/update/{_id}")
def update_teacher(teacher: Teacher, _id: int):
    status = data.update_id(teacher, _id)
    if status:
        return {"message": "Successful !!", "result": "teacher updated :D"}
    else:
        raise HTTPException(status_code=404, detail=f"teacher with id {_id} not found")


@app.patch("/course/update/{_id}")
def update_course(course: Course, _id: int):
    status = data.update_id(course, _id)
    if status:
        return {"message": "Successful !!", "result": "course updated :D"}
    else:
        raise HTTPException(status_code=404, detail=f"course with id {_id} not found")
