from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional, List
from enum import Enum

class AttendanceStatusEnum(str, Enum):
    PRESENT = "present"
    ABSENT = "absent"

class AttendanceBase(BaseModel):
    date: date
    status: AttendanceStatusEnum

class AttendanceCreate(AttendanceBase):
    employee_id: int

class AttendanceResponse(AttendanceBase):
    id: int
    employee_id: int

    class Config:
        orm_mode = True

class EmployeeBase(BaseModel):
    employee_id: str = Field(..., min_length=1, max_length=50)
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    department: str = Field(..., min_length=1, max_length=100)

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None

class EmployeeResponse(EmployeeBase):
    id: int
    created_at: date
    attendance_records: List[AttendanceResponse] = []

    class Config:
        orm_mode = True

class ErrorResponse(BaseModel):
    detail: str
    status_code: int
