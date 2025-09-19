from sqlalchemy.orm import Session
import models

# ---------------------------
# Teacher CRUD
# ---------------------------

def create_teacher(db: Session, name: str, subject: str):
    teacher = models.Teacher(name=name, subject=subject)
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher

def get_teachers(db: Session):
    return db.query(models.Teacher).all()

def get_teacher(db: Session, teacher_id: int):
    return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()

def update_teacher(db: Session, teacher_id: int, name: str = None, subject: str = None):
    teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if teacher:
        if name:
            teacher.name = name
        if subject:
            teacher.subject = subject
        db.commit()
        db.refresh(teacher)
    return teacher

def delete_teacher(db: Session, teacher_id: int):
    teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if teacher:
        db.delete(teacher)
        db.commit()
    return teacher


# ---------------------------
# Student CRUD
# ---------------------------

def create_student(db: Session, name: str, age: int, teacher_id: int):
    student = models.Student(name=name, age=age, teacher_id=teacher_id)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def get_students(db: Session):
    return db.query(models.Student).all()

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def update_student(db: Session, student_id: int, name: str = None, age: int = None, teacher_id: int = None):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        if name:
            student.name = name
        if age:
            student.age = age
        if teacher_id:
            student.teacher_id = teacher_id
        db.commit()
        db.refresh(student)
    return student

def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student
