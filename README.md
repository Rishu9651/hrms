# HRMS - Human Resource Management System

A lightweight, full-stack web application for managing employee records and daily attendance. Built with React, FastAPI, and SQLAlchemy.

## Live Demo

- Frontend: https://hrms.vercel.app
- API Docs: https://hrms-api.onrender.com/docs

## Overview

HRMS is a production-ready HR management system designed for small to medium-sized organizations. It provides essential HR functions with a clean, intuitive interface.

### Key Features

Employee Management
- Add, view, edit, and delete employee records
- Unique employee IDs and email validation
- Department categorization
- Search and filter employees

Attendance Tracking
- Mark daily attendance (Present/Absent)
- View attendance history per employee
- Filter and sort attendance records
- Attendance statistics (total, present, absent days)

Professional UI
- Responsive design (mobile, tablet, desktop)
- Clean, modern interface
- Real-time validation and error feedback
- Loading and empty states
- Success notifications

Production Ready
- RESTful API with proper error handling
- Database persistence (SQLite/PostgreSQL)
- Input validation and security
- Proper HTTP status codes
- CORS enabled for cross-origin requests

## Tech Stack

### Frontend
- **React 18** - UI library
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **Axios** - HTTP client
- **JavaScript (ES6+)** - Language

### Backend
- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **SQLAlchemy** - ORM
- **Pydantic** - Data validation
- **Python 3.8+** - Language

### Database
- **SQLite** - Development
- **PostgreSQL** - Production (recommended)

```
hrms/
├── hrms-backend/               # FastAPI backend
│   ├── main.py                 # Application with all routes
│   ├── models.py               # Database models
│   ├── schemas.py              # Pydantic validation schemas
│   ├── database.py             # Database configuration
│   ├── requirements.txt        # Python dependencies
│   ├── .env                    # Environment variables
│   └── README.md               # Backend documentation
│
├── hrms-frontend/              # React frontend
│   ├── src/
│   │   ├── main.jsx            # Entry point
│   │   ├── App.jsx             # Main component
│   │   ├── api.js              # API client
│   │   ├── index.css           # Global styles
│   │   └── components/         # React components
│   ├── package.json            # NPM dependencies
│   ├── vite.config.js          # Vite config
│   ├── tailwind.config.js      # Tailwind config
│   ├── .env.example            # Environment template
│   └── README.md               # Frontend documentation
│
└── README.md                   # This file
```

## Quick Start

### Prerequisites
- Node.js v18+ and npm v10+
- Python 3.8+ and pip
- Git

### Backend Setup (Local)

1. **Navigate to backend directory**:
   ```bash
   cd hrms-backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run development server**:
   ```bash
   python main.py
   ```
   
   Backend will be available at http://localhost:8000
   
   - Swagger UI: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

### Frontend Setup (Local)

1. **Navigate to frontend directory**:
   ```bash
   cd hrms-frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Create .env file**:
   ```bash
   cp .env.example .env
   ```
   
   Ensure VITE_API_URL=http://localhost:8000/api

4. **Run development server**:
   ```bash
   npm run dev
   ```
   
   Frontend will be available at http://localhost:3000

### Running Both Applications

Open two terminal windows:

Terminal 1 - Backend:
```bash
cd hrms-backend
source venv/bin/activate
python main.py
```

Terminal 2 - Frontend:
```bash
cd hrms-frontend
npm run dev
```

Visit http://localhost:3000 to use the application.

## API Documentation

### Base URL
```
Local: http://localhost:8000/api
Production: https://hrms-api.onrender.com/api
```

### Employees
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/employees` | Get all employees |
| POST | `/employees` | Create new employee |
| GET | `/employees/{id}` | Get specific employee |
| PUT | `/employees/{id}` | Update employee |
| DELETE | `/employees/{id}` | Delete employee |

### Attendance
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/attendance` | Get all attendance records |
| POST | `/attendance` | Mark attendance |
| GET | `/attendance/employee/{employee_id}` | Get employee's attendance |
| PUT | `/attendance/{id}` | Update attendance |
| DELETE | `/attendance/{id}` | Delete attendance record |

### Statistics
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/stats/employees/count` | Total employee count |
| GET | `/stats/employees/{employee_id}/attendance-summary` | Attendance summary |

### Health Check
```
GET /health
```

### API Documentation (Interactive)
```
GET /docs (Swagger UI)
GET /redoc (ReDoc)
```

## Configuration

### Backend Environment Variables
```env
# Database
DATABASE_URL=postgresql://user:password@localhost/hrms

# Environment
ENVIRONMENT=production
DEBUG=false
```

### Frontend Environment Variables
```env
# API Endpoint
VITE_API_URL=https://hrms-api.onrender.com/api
```


