from pydantic import BaseModel
from typing import ClassVar, List


class Student(BaseModel):
    id: int = -1
    name: str = ""
    age: int = 0
    enrolled_courses: List[int] = []  # Course ID
    entity: ClassVar[str] = "student"


class Teacher(BaseModel):
    id: int = -1
    name: str = ""
    age: int = 0
    teaching: List[int] = []
    entity: ClassVar[str] = "teacher"


class Course(BaseModel):
    id: int = -1
    name: str = ""
    entity: ClassVar[str] = "courses"
