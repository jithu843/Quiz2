 . import models, schemas
from sqlalchemy.orm import Session

def create_employee(db: Session, emp: schemas.EmployeeCreate):
    db_emp = models.Employee(**emp.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()
