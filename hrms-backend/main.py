from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import date
from typing import List

from database import engine, get_db, Base
from models import Employee, Attendance, AttendanceStatus
from schemas import (
    EmployeeCreate, EmployeeResponse, EmployeeUpdate,
    AttendanceCreate, AttendanceResponse
)

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HRMS Lite API",
    description="Lightweight Human Resource Management System",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== EMPLOYEE ENDPOINTS ====================

@app.post("/api/employees", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """Create a new employee"""
    
    # Check if employee_id already exists
    existing_employee = db.query(Employee).filter(Employee.employee_id == employee.employee_id).first()
    if existing_employee:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Employee ID '{employee.employee_id}' already exists"
        )
    
    # Check if email already exists
    existing_email = db.query(Employee).filter(Employee.email == employee.email).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Email '{employee.email}' already in use"
        )
    
    db_employee = Employee(
        employee_id=employee.employee_id,
        name=employee.name,
        email=employee.email,
        department=employee.department
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.get("/api/employees", response_model=List[EmployeeResponse])
def get_all_employees(db: Session = Depends(get_db)):
    """Get all employees"""
    employees = db.query(Employee).all()
    return employees

@app.get("/api/employees/{employee_id_param}", response_model=EmployeeResponse)
def get_employee(employee_id_param: int, db: Session = Depends(get_db)):
    """Get a specific employee by ID"""
    employee = db.query(Employee).filter(Employee.id == employee_id_param).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id_param} not found"
        )
    return employee

@app.put("/api/employees/{employee_id_param}", response_model=EmployeeResponse)
def update_employee(employee_id_param: int, employee_update: EmployeeUpdate, db: Session = Depends(get_db)):
    """Update an employee"""
    employee = db.query(Employee).filter(Employee.id == employee_id_param).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id_param} not found"
        )
    
    # Check if new email is already in use
    if employee_update.email and employee_update.email != employee.email:
        existing_email = db.query(Employee).filter(Employee.email == employee_update.email).first()
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Email '{employee_update.email}' already in use"
            )
    
    update_data = employee_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(employee, field, value)
    
    db.commit()
    db.refresh(employee)
    return employee

@app.delete("/api/employees/{employee_id_param}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id_param: int, db: Session = Depends(get_db)):
    """Delete an employee"""
    employee = db.query(Employee).filter(Employee.id == employee_id_param).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id_param} not found"
        )
    db.delete(employee)
    db.commit()
    return None

# ==================== ATTENDANCE ENDPOINTS ====================

@app.post("/api/attendance", response_model=AttendanceResponse, status_code=status.HTTP_201_CREATED)
def mark_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    """Mark attendance for an employee"""
    
    # Check if employee exists
    employee = db.query(Employee).filter(Employee.id == attendance.employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {attendance.employee_id} not found"
        )
    
    # Check if attendance for this employee on this date already exists
    existing_record = db.query(Attendance).filter(
        Attendance.employee_id == attendance.employee_id,
        Attendance.date == attendance.date
    ).first()
    
    if existing_record:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Attendance already marked for this employee on {attendance.date}"
        )
    
    db_attendance = Attendance(
        employee_id=attendance.employee_id,
        date=attendance.date,
        status=attendance.status
    )
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

@app.get("/api/attendance", response_model=List[AttendanceResponse])
def get_all_attendance(db: Session = Depends(get_db)):
    """Get all attendance records"""
    records = db.query(Attendance).all()
    return records

@app.get("/api/attendance/employee/{employee_id_param}", response_model=List[AttendanceResponse])
def get_employee_attendance(employee_id_param: int, db: Session = Depends(get_db)):
    """Get attendance records for a specific employee"""
    
    # Check if employee exists
    employee = db.query(Employee).filter(Employee.id == employee_id_param).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id_param} not found"
        )
    
    records = db.query(Attendance).filter(Attendance.employee_id == employee_id_param).all()
    return records

@app.put("/api/attendance/{attendance_id}", response_model=AttendanceResponse)
def update_attendance(attendance_id: int, attendance_update: AttendanceCreate, db: Session = Depends(get_db)):
    """Update an attendance record"""
    
    record = db.query(Attendance).filter(Attendance.id == attendance_id).first()
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attendance record with ID {attendance_id} not found"
        )
    
    record.status = attendance_update.status
    db.commit()
    db.refresh(record)
    return record

@app.delete("/api/attendance/{attendance_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_attendance(attendance_id: int, db: Session = Depends(get_db)):
    """Delete an attendance record"""
    
    record = db.query(Attendance).filter(Attendance.id == attendance_id).first()
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attendance record with ID {attendance_id} not found"
        )
    
    db.delete(record)
    db.commit()
    return None

# ==================== STATS ENDPOINTS ====================

@app.get("/api/stats/employees/count")
def get_employee_count(db: Session = Depends(get_db)):
    """Get total employee count"""
    count = db.query(Employee).count()
    return {"total_employees": count}

@app.get("/api/stats/employees/{employee_id_param}/attendance-summary")
def get_employee_attendance_summary(employee_id_param: int, db: Session = Depends(get_db)):
    """Get attendance summary for an employee"""
    
    employee = db.query(Employee).filter(Employee.id == employee_id_param).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id_param} not found"
        )
    
    total_records = db.query(Attendance).filter(Attendance.employee_id == employee_id_param).count()
    present_count = db.query(Attendance).filter(
        Attendance.employee_id == employee_id_param,
        Attendance.status == AttendanceStatus.PRESENT
    ).count()
    absent_count = db.query(Attendance).filter(
        Attendance.employee_id == employee_id_param,
        Attendance.status == AttendanceStatus.ABSENT
    ).count()
    
    return {
        "employee_id": employee_id_param,
        "employee_name": employee.name,
        "total_records": total_records,
        "present_days": present_count,
        "absent_days": absent_count
    }

# ==================== HEALTH CHECK ====================

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "ok", "message": "HRMS Lite API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
