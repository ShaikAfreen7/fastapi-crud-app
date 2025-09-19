from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, crud
from database import engine, get_db

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ---------------------------
# Teacher Routes
# ---------------------------

@app.post("/teachers/")
def create_teacher(name: str, subject: str, db: Session = Depends(get_db)):
    return crud.create_teacher(db=db, name=name, subject=subject)

@app.get("/teachers/")
def get_teachers(db: Session = Depends(get_db)):
    return crud.get_teachers(db)

@app.get("/teachers/{teacher_id}")
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    return crud.get_teacher(db, teacher_id)

@app.put("/teachers/{teacher_id}")
def update_teacher(teacher_id: int, name: str = None, subject: str = None, db: Session = Depends(get_db)):
    return crud.update_teacher(db, teacher_id, name, subject)

@app.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    return crud.delete_teacher(db, teacher_id)


# ---------------------------
# Student Routes
# ---------------------------

@app.post("/students/")
def create_student(name: str, age: int, teacher_id: int, db: Session = Depends(get_db)):
    return crud.create_student(db=db, name=name, age=age, teacher_id=teacher_id)

@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    return crud.get_student(db, student_id)

@app.put("/students/{student_id}")
def update_student(student_id: int, name: str = None, age: int = None, teacher_id: int = None, db: Session = Depends(get_db)):
    return crud.update_student(db, student_id, name, age, teacher_id)

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db, student_id)
