from app import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, DateTime
from datetime import datetime


class Student(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(String(10), unique=True)
    insert_time = Column(DateTime, default=datetime.now)

    task_data = db.relationship("TaskData", backref='student')

    def __init__(self, name, number):
        self.name = name
        self.number = number


class TaskData(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

    student_id = db.Column(Integer, ForeignKey('student.number'))

    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score
