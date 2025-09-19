from fastapi import FastAPI, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD App")
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root
@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Teachers
@app.get("/teachers")
def read_teachers(request: Request, db: Session = Depends(get_db)):
    teachers = crud.get_teachers(db)
    return templates.TemplateResponse("teachers.html", {"request": request, "teachers": teachers})

@app.post("/teachers/create")
def add_teacher(request: Request, name: str = Form(...), subject: str = Form(...), db: Session = Depends(get_db)):
    crud.create_teacher(db, name, subject)
    return RedirectResponse(url="/teachers", status_code=303)

# Students
@app.get("/students")
def read_students(request: Request, db: Session = Depends(get_db)):
    students = crud.get_students(db)
    return templates.TemplateResponse("students.html", {"request": request, "students": students})

@app.post("/students/create")
def add_student(request: Request, name: str = Form(...), age: int = Form(...), teacher_id: int = Form(...), db: Session = Depends(get_db)):
    crud.create_student(db, name, age, teacher_id)
    return RedirectResponse(url="/students", status_code=303)
