from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    age: int
    department: str
    position: str
    salary: float
    performance_score: float

class EmployeeRead(EmployeeCreate):
    id: int
    class Config:
        orm_mode = True
