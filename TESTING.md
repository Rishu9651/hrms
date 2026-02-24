# HRMS Lite - Testing Guide

This guide covers testing procedures for the HRMS Lite application.

## Quick Start Testing

### 1. Start Backend

```bash
cd hrms-lite-backend

# Create virtual environment (first time only)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies (first time only)
pip install -r requirements.txt

# Start server
python main.py
```

Backend running at: `http://localhost:8000`

### 2. Start Frontend

In a **new terminal**:

```bash
cd hrms-lite-frontend

# Install dependencies (first time only)
npm install

# Start dev server
npm run dev
```

Frontend running at: `http://localhost:3000`

### 3. Access Application

Open browser and go to: `http://localhost:3000`

## Manual Testing Scenarios

### Employee Management

#### Test Case 1: Add Employee
- [ ] Click "Add Employee" button
- [ ] Fill in all required fields:
  - Employee ID: `EMP001`
  - Name: `John Doe`
  - Email: `john@example.com`
  - Department: `Engineering`
- [ ] Click "Save"
- [ ] Verify employee appears in list
- [ ] Verify success message appears

#### Test Case 2: Employee Validation
- [ ] Try adding employee with:
  - [ ] Duplicate Employee ID (should show error)
  - [ ] Duplicate Email (should show error)
  - [ ] Invalid Email format (should show error)
  - [ ] Missing required field (should show error)
- [ ] Verify error messages are clear

#### Test Case 3: Search Employees
- [ ] Add multiple employees
- [ ] Search by Employee ID:
  - [ ] Type "EMP001"
  - [ ] Verify only matching employee shows
- [ ] Search by Name:
  - [ ] Type "john"
  - [ ] Verify matching employees show
- [ ] Search by Email:
  - [ ] Type "example.com"
  - [ ] Verify matching employees show
- [ ] Clear search
  - [ ] All employees display again

#### Test Case 4: Edit Employee
- [ ] Click "Edit" on an employee
- [ ] Change name and email
- [ ] Click "Save"
- [ ] Verify employee details updated
- [ ] Verify employee ID is disabled (read-only)

#### Test Case 5: Delete Employee
- [ ] Click "Delete" on an employee
- [ ] Confirm deletion dialog
- [ ] Click "OK"
- [ ] Verify employee removed from list
- [ ] Verify success message

### Attendance Management

#### Test Case 6: Mark Attendance
- [ ] Click "Attendance" tab
- [ ] Select an employee from dropdown
- [ ] Click "Mark Attendance"
- [ ] Fill form:
  - [ ] Date: Select today's date
  - [ ] Status: Select "Present"
- [ ] Click "Mark"
- [ ] Verify attendance record appears below
- [ ] Verify success message

#### Test Case 7: Mark Multiple Attendance
- [ ] Mark attendance for same employee on different dates
- [ ] Verify all records show in list
- [ ] Verify date format is readable (e.g., "February 24, 2026")

#### Test Case 8: Attendance Validation
- [ ] Try marking attendance for same employee on same date twice
- [ ] Verify error message about duplicate attendance
- [ ] Verify can't select future dates

#### Test Case 9: Filter Attendance
- [ ] Mark both Present and Absent attendance for an employee
- [ ] Test "Filter by Status":
  - [ ] Select "Present" - only Present records show
  - [ ] Select "Absent" - only Absent records show
  - [ ] Select "All" - all records show

#### Test Case 10: Sort Attendance
- [ ] Mark attendance on multiple dates
- [ ] Test "Sort by Date":
  - [ ] "Newest First" - most recent date first
  - [ ] "Oldest First" - oldest date first

#### Test Case 11: Attendance Statistics
- [ ] Mark attendance to create both Present and Absent days
- [ ] Verify stats cards show:
  - [ ] Total Records: Correct count
  - [ ] Days Present: Correct count
  - [ ] Days Absent: Correct count

#### Test Case 12: Delete Attendance
- [ ] Click "Delete" on an attendance record
- [ ] Confirm dialog
- [ ] Verify record removed
- [ ] Verify stats updated

### UI/UX Testing

#### Test Case 13: Loading States
- [ ] Observe loading spinner when:
  - [ ] First loading employees list
  - [ ] Marking attendance
  - [ ] Form submission
- [ ] Verify spinners show and disappear appropriately

#### Test Case 14: Empty States
- [ ] Delete all employees
- [ ] Verify empty state message appears
- [ ] Add new employee
- [ ] Verify list updates immediately

#### Test Case 15: Navigation
- [ ] Click between "Employees" and "Attendance" tabs
- [ ] Verify content switches smoothly
- [ ] Verify state persists (selected employee remains selected)

#### Test Case 16: Responsive Design
- [ ] On desktop browser:
  - [ ] Open to full width
  - [ ] Verify layout is proper
- [ ] Test tablet view:
  - [ ] Open DevTools (F12)
  - [ ] Set viewport to 768px width
  - [ ] Verify responsive layout
- [ ] Test mobile view:
  - [ ] Set viewport to 375px width
  - [ ] Verify layout is usable
  - [ ] Verify table scrolls horizontally if needed

#### Test Case 17: Error Handling
- [ ] Stop backend server
- [ ] Try to load employees
- [ ] Verify error message appears
- [ ] Restart backend
- [ ] Verify data loads again

### API Testing (Using Swagger UI)

Open `http://localhost:8000/docs` in browser

#### Test Case 18: API Documentation
- [ ] Verify all endpoints are documented
- [ ] Verify request/response schemas are correct
- [ ] Click "Try it out" on any endpoint

#### Test Case 19: Create Employee via API
- [ ] Click on `POST /api/employees`
- [ ] Click "Try it out"
- [ ] Enter request body:
  ```json
  {
    "employee_id": "EMP999",
    "name": "API Test User",
    "email": "apitest@example.com",
    "department": "Testing"
  }
  ```
- [ ] Click "Execute"
- [ ] Verify 201 Created status
- [ ] Verify response contains created employee
- [ ] Refresh frontend to see new employee

#### Test Case 20: Get Employees via API
- [ ] Click on `GET /api/employees`
- [ ] Click "Try it out" → "Execute"
- [ ] Verify 200 status
- [ ] Verify response is array of all employees

#### Test Case 21: Mark Attendance via API
- [ ] Click on `POST /api/attendance`
- [ ] Click "Try it out"
- [ ] Enter request body:
  ```json
  {
    "employee_id": 1,
    "date": "2026-02-24",
    "status": "present"
  }
  ```
- [ ] Click "Execute"
- [ ] Verify 201 status

#### Test Case 22: Health Check
- [ ] Click on `GET /health`
- [ ] Click "Try it out" → "Execute"
- [ ] Verify 200 status
- [ ] Verify response: `{"status":"ok","message":"HRMS Lite API is running"}`

## Edge Cases & Error Scenarios

### Employee Management Edge Cases
- [ ] Add employee with very long name (100+ chars)
- [ ] Add employee with special characters in name
- [ ] Add employee with international email domains
- [ ] Delete employee and verify attendance records are also deleted
- [ ] Search with uppercase, lowercase, and mixed case
- [ ] Try to add employee with email containing uppercase (case-insensitive check)

### Attendance Edge Cases
- [ ] Mark attendance for yesterday, today, and tomorrow (tomorrow should fail)
- [ ] Mark same attendance twice on same date (should fail)
- [ ] View attendance summary for employee with 0 records
- [ ] Filter/sort with 1 record (should work)
- [ ] Filter/sort with 100+ records (performance test)

## Performance Testing

### Load Testing - Employees
1. Add 100 employees
2. Search functionality still responsive:
   - [ ] Search returns results < 500ms
3. Table renders without lag
4. Scrolling smooth

### Load Testing - Attendance  
1. Mark 500+ attendance records for an employee
2. Records load without lag:
   - [ ] Initial load < 2 seconds
   - [ ] Filter/sort < 500ms
3. Stats calculate correctly despite large dataset

## Browser Testing

Test on:
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)

Verify:
- [ ] No console errors
- [ ] Styling consistent
- [ ] Forms work
- [ ] API calls work

## Database Testing

### SQLite (Development)

1. Check database file created:
   ```bash
   ls -la hrms.db
   ```

2. Access database directly:
   ```bash
   sqlite3 hrms.db

   # View tables
   .tables

   # View schema
   .schema

   # Query employees
   SELECT * FROM employees;

   # Exit
   .exit
   ```

### PostgreSQL (Production)

Connect to database:
```bash
psql <DATABASE_URL>

# View tables
\dt

# View schema
\d employees
\d attendance

# Query
SELECT * FROM employees;
```

## Regression Testing Checklist

After any code change, verify:

- [ ] Employee CRUD operations work
- [ ] Attendance CRUD operations work
- [ ] Search functionality works
- [ ] Validation errors display correctly
- [ ] API documentation is accessible
- [ ] No console errors
- [ ] No network errors
- [ ] UI renders correctly
- [ ] Responsive design works

## Test Data Script

Create test data quickly:

```bash
# Copy to clipboard and paste in Swagger UI or use curl

# Employee 1
{
  "employee_id": "EMP001",
  "name": "Alice Johnson",
  "email": "alice@company.com",
  "department": "Engineering"
}

# Employee 2  
{
  "employee_id": "EMP002",
  "name": "Bob Smith",
  "email": "bob@company.com",
  "department": "Sales"
}

# Employee 3
{
  "employee_id": "EMP003",
  "name": "Carol Williams",
  "email": "carol@company.com",
  "department": "Marketing"
}
```

## Continuous Testing

For CI/CD pipeline, consider:
- Unit tests for APIs (pytest)
- Component tests for React (React Testing Library)
- E2E tests (Playwright/Cypress)
- API integration tests
- Performance benchmarks
- Cross-browser testing (BrowserStack)

## Known Limitations

- ✋ No authentication (assumed single admin user)
- ✋ Single timezone (UTC)
- ✋ No audit logging
- ✋ Limited to one organization
- ✋ Dates stored without time component

## Reporting Issues

When reporting bugs, include:
1. Step to reproduce
2. Expected behavior
3. Actual behavior
4. Browser/OS version
5. Console errors (if any)
6. Network errors (if any)
7. Screenshot/video if helpful

---

**Last Updated**: February 24, 2026
