from sqlalchemy import Column, Integer, String, Date, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from database import Base

class AttendanceStatus(str, enum.Enum):
    PRESENT = "present"
    ABSENT = "absent"

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    department = Column(String)
    created_at = Column(Date, default=datetime.utcnow)

    attendance_records = relationship("Attendance", back_populates="employee", cascade="all, delete-orphan")

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, index=True)
    date = Column(Date)
    status = Column(Enum(AttendanceStatus), default=AttendanceStatus.PRESENT)
    created_at = Column(Date, default=datetime.utcnow)

    employee = relationship("Employee", back_populates="attendance_records")
