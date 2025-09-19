from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
import os

# Ensure tables are created
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD App")

# ---------------------------
# Dependency to get DB session
# ---------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------------
# Root route
# ---------------------------
@app.get("/")
def root():
    return {"message": "Welcome to FastAPI CRUD App!"}

# ---------------------------
# CRUD Endpoints
# ---------------------------

# Create Teacher
@app.post("/teachers/")
def create_teacher(name: str, subject: str, db: Session = Depends(get_db)):
    teacher = models.Teacher(name=name, subject=subject)
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher

# Get all Teachers
@app.get("/teachers/")
def get_teachers(db: Session = Depends(get_db)):
    return db.query(models.Teacher).all()

# Create Student
@app.post("/students/")
def create_student(name: str, age: int, teacher_id: int, db: Session = Depends(get_db)):
    student = models.Student(name=name, age=age, teacher_id=teacher_id)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

# Get all Students
@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()
