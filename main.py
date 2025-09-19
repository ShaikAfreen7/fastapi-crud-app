from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, crud
from database import SessionLocal, engine

# Create tables if not exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency: get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------------
# CRUD Endpoints
# ---------------------------

@app.post("/teachers/")
def create_teacher(name: str, subject: str, db: Session = Depends(get_db)):
    return crud.create_teacher(db, name, subject)

@app.get("/teachers/")
def get_teachers(db: Session = Depends(get_db)):
    return crud.get_teachers(db)

@app.post("/students/")
def create_student(name: str, age: int, teacher_id: int, db: Session = Depends(get_db)):
    return crud.create_student(db, name, age, teacher_id)

@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)
