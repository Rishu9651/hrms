# HRMS Lite Backend

FastAPI-based backend for the Human Resource Management System (HRMS Lite).

## Tech Stack

- **Framework**: FastAPI
- **Database**: SQLite (dev) / PostgreSQL (production)
- **ORM**: SQLAlchemy
- **Server**: Uvicorn
- **Validation**: Pydantic

## Project Structure

```
hrms-lite-backend/
├── main.py           # Main application entry point with all routes
├── models.py         # SQLAlchemy database models
├── schemas.py        # Pydantic validation schemas  
├── database.py       # Database configuration
├── requirements.txt  # Python dependencies
├── .env              # Environment variables
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Local Development

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**:
   ```bash
   python main.py
   ```
   Or with Uvicorn directly:
   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`
   - **API Docs**: `http://localhost:8000/docs` (Swagger UI)
   - **Health Check**: `http://localhost:8000/health`

## API Endpoints

### Employee Management

- **GET** `/api/employees` - Get all employees
- **POST** `/api/employees` - Create new employee
- **GET** `/api/employees/{id}` - Get specific employee
- **PUT** `/api/employees/{id}` - Update employee
- **DELETE** `/api/employees/{id}` - Delete employee

### Attendance Management

- **GET** `/api/attendance` - Get all attendance records
- **POST** `/api/attendance` - Mark attendance
- **GET** `/api/attendance/employee/{employee_id}` - Get employee attendance records
- **PUT** `/api/attendance/{id}` - Update attendance record
- **DELETE** `/api/attendance/{id}` - Delete attendance record

### Statistics

- **GET** `/api/stats/employees/count` - Get total employee count
- **GET** `/api/stats/employees/{employee_id}/attendance-summary` - Get attendance summary for an employee

## Environment Variables

```env
DATABASE_URL=sqlite:///./hrms.db
ENVIRONMENT=development
DEBUG=true
```

For PostgreSQL:
```env
DATABASE_URL=postgresql://user:password@localhost/hrms
```

## Database Models

### Employee
- `id`: Primary key
- `employee_id`: Unique employee identifier
- `name`: Employee full name
- `email`: Employee email address
- `department`: Department name
- `created_at`: Creation timestamp

### Attendance
- `id`: Primary key
- `employee_id`: Foreign key to Employee
- `date`: Attendance date
- `status`: Present/Absent
- `created_at`: Creation timestamp

## Error Handling

All errors return meaningful HTTP status codes and messages:
- `400 Bad Request`: Validation errors or duplicate records
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

## CORS Configuration

CORS is enabled for all origins. Update the CORS middleware in `main.py` for production:
```python
allow_origins=["https://your-frontend-url.com"]
```

## Deployment

The backend is production-ready and can be deployed to:
- Render (recommended)
- Railway
- Heroku
- AWS
- Google Cloud Platform

### Deployment Requirements

1. Database: Use PostgreSQL instead of SQLite
2. Update `DATABASE_URL` environment variable
3. Set `DEBUG=false`
4. Update CORS allowed origins
5. Use a production ASGI server (Uvicorn handles this)

## Testing Endpoints

Use cURL or Postman to test:

```bash
# Get all employees
curl http://localhost:8000/api/employees

# Create employee
curl -X POST http://localhost:8000/api/employees \
  -H "Content-Type: application/json" \
  -d '{"employee_id":"EMP001","name":"John Doe","email":"john@example.com","department":"Engineering"}'

# Mark attendance
curl -X POST http://localhost:8000/api/attendance \
  -H "Content-Type: application/json" \
  -d '{"employee_id":1,"date":"2024-02-24","status":"present"}'

# Health check
curl http://localhost:8000/health
```

## Notes

- The backend creates tables automatically on startup
- SQLite database file is created in the project root (`hrms.db`)
- All timestamps are stored as dates (not full datetime)
- Employee ID must be unique and cannot be changed after creation
- Email validation is strict (RFC 5321)
