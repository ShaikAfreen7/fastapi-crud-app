from sqlalchemy.orm import Session
import models

# Teacher CRUD
def create_teacher(db: Session, name: str, subject: str):
    teacher = models.Teacher(name=name, subject=subject)
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher

def get_teachers(db: Session):
    return db.query(models.Teacher).all()

# Student CRUD
def create_student(db: Session, name: str, age: int, teacher_id: int):
    student = models.Student(name=name, age=age, teacher_id=teacher_id)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def get_students(db: Session):
    return db.query(models.Student).all()
