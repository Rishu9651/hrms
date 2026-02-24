# HRMS Lite - Human Resource Management System

A lightweight, full-stack web application for managing employee records and daily attendance. Built with React, FastAPI, and SQLAlchemy.

## 🚀 Live Demo

- **Frontend**: [https://hrms-lite.vercel.app](https://hrms-lite.vercel.app)
- **API Docs**: [https://hrms-lite-api.onrender.com/docs](https://hrms-lite-api.onrender.com/docs)

## 📋 Overview

HRMS Lite is a production-ready HR management system designed for small to medium-sized organizations. It provides essential HR functions with a clean, intuitive interface.

### Key Features

✅ **Employee Management**
- Add, view, edit, and delete employee records
- Unique employee IDs and email validation
- Department categorization
- Search and filter employees

✅ **Attendance Tracking**
- Mark daily attendance (Present/Absent)
- View attendance history per employee
- Filter and sort attendance records
- Attendance statistics (total, present, absent days)

✅ **Professional UI**
- Responsive design (mobile, tablet, desktop)
- Clean, modern interface
- Real-time validation and error feedback
- Loading and empty states
- Success notifications

✅ **Production Ready**
- RESTful API with proper error handling
- Database persistence (SQLite/PostgreSQL)
- Input validation and security
- Proper HTTP status codes
- CORS enabled for cross-origin requests

## 🛠️ Tech Stack

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

## 📁 Project Structure

```
hrms-lite/
├── hrms-lite-backend/          # FastAPI backend
│   ├── main.py                 # Application with all routes
│   ├── models.py               # Database models
│   ├── schemas.py              # Pydantic validation schemas
│   ├── database.py             # Database configuration
│   ├── requirements.txt        # Python dependencies
│   ├── .env                    # Environment variables
│   └── README.md               # Backend documentation
│
├── hrms-lite-frontend/         # React frontend
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

## 🚀 Quick Start

### Prerequisites
- Node.js v18+ and npm v10+
- Python 3.8+ and pip
- Git

### Backend Setup (Local)

1. **Navigate to backend directory**:
   ```bash
   cd hrms-lite-backend
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
   
   Backend will be available at `http://localhost:8000`
   
   - **Swagger UI**: `http://localhost:8000/docs`
   - **Health Check**: `http://localhost:8000/health`

### Frontend Setup (Local)

1. **Navigate to frontend directory**:
   ```bash
   cd hrms-lite-frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Create .env file**:
   ```bash
   cp .env.example .env
   ```
   
   Ensure `VITE_API_URL=http://localhost:8000/api`

4. **Run development server**:
   ```bash
   npm run dev
   ```
   
   Frontend will be available at `http://localhost:3000`

### Running Both Applications

Open two terminal windows:

**Terminal 1 - Backend**:
```bash
cd hrms-lite-backend
source venv/bin/activate
python main.py
```

**Terminal 2 - Frontend**:
```bash
cd hrms-lite-frontend
npm run dev
```

Visit `http://localhost:3000` to use the application.

## 📚 API Documentation

### Base URL
```
Local: http://localhost:8000/api
Production: https://hrms-lite-api.onrender.com/api
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

## 🔧 Configuration

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
VITE_API_URL=https://hrms-lite-api.onrender.com/api
```

## 📤 Deployment

### Backend Deployment (Render)

1. Push code to GitHub
2. Create new Web Service on Render
3. Connect GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 8000`
5. Add environment variables:
   - `DATABASE_URL`: PostgreSQL connection string
   - `ENVIRONMENT`: production
   - `DEBUG`: false
6. Deploy

### Frontend Deployment (Vercel)

1. Push code to GitHub
2. Import project on Vercel
3. Configure:
   - **Framework**: Vite
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
4. Add environment variable:
   - `VITE_API_URL`: Backend API URL
5. Deploy

## ✅ Testing

### API Testing
Use Swagger UI at `/docs` (backend running)

### Manual Testing Checklist
- [ ] Add employee with all required fields
- [ ] View all employees in list
- [ ] Edit employee details
- [ ] Delete employee
- [ ] Search employees by name/ID/email
- [ ] Mark attendance for employee
- [ ] View attendance records with filters
- [ ] Sort attendance by date
- [ ] Delete attendance record
- [ ] View attendance statistics
- [ ] Test error cases (duplicates, invalid email, etc.)

## 🎯 Core Functional Requirements Met

✅ **Employee Management**
- Add employee with ID, name, email, department
- View all employees
- Delete employee
- Validation and error handling

✅ **Attendance Management**
- Mark attendance with date and status
- View attendance records per employee
- Delete attendance records
- Statistics tracking

✅ **Backend**
- RESTful APIs for all operations
- Database persistence
- Server-side validation
- Proper error handling
- Meaningful HTTP status codes

✅ **Frontend**
- Professional, production-ready UI
- Responsive design
- Form validation
- Error and success messages
- Loading states

✅ **Deployment**
- Live frontend URL (Vercel)
- Live backend API (Render)
- Public GitHub repository
- Comprehensive documentation

## 📊 Bonus Features Implemented

✅ Attendance filtering by status
✅ Sort attendance records by date  
✅ Attendance statistics dashboard
✅ Search functionality for employees
✅ Department categorization
✅ Professional error handling
✅ Real-time validation feedback
✅ Responsive mobile design
✅ API documentation with Swagger UI

## 📝 Assumptions & Limitations

### Assumptions
1. Single admin user (no authentication required)
2. Small-to-medium organization scope
3. One organization per deployment
4. Dates stored without time components
5. SQLite for development, PostgreSQL for production

### Limitations
1. No multi-user authentication
2. No role-based access control
3. No advanced HR features (payroll, leave management)
4. No file uploads
5. No audit logging of changes
6. No backup/recovery system
7. Single timezone (UTC)

## 🔒 Security Considerations

- Email validation (RFC 5321)
- CORS configured (customize for production)
- SQL injection prevention via SQLAlchemy ORM
- Input validation with Pydantic
- No sensitive data in logs
- Environment variables for secrets

## 🐛 Troubleshooting

### Backend won't start
- Check Python version (3.8+)
- Verify dependencies: `pip install -r requirements.txt`
- Check if port 8000 is available
- Review error messages in terminal

### Frontend can't connect to API
- Verify backend is running on port 8000
- Check `VITE_API_URL` in `.env`
- Check browser console for CORS errors
- Ensure CORS is enabled in backend

### Database errors
- If using SQLite, ensure `hrms.db` file exists and is writable
- If using PostgreSQL, verify connection string in `.env`
- Check database permissions

## 📞 Support

For issues or questions:
1. Check the respective README files (backend/frontend)
2. Review API documentation at `/docs` (backend)
3. Check browser console for frontend errors
4. Review server logs for backend errors

## 📄 License

This project is provided as-is for educational and commercial use.

## 🎓 Learning Outcomes

This project demonstrates:
- Full-stack web development with modern tools
- RESTful API design and implementation
- Database design and ORM usage
- Frontend framework (React) best practices
- Component-based architecture
- Real-world form validation and error handling
- Responsive UI design
- Deployment and DevOps basics
- Git workflow and version control

## 🚀 Future Enhancements

Potential features for future versions:
- User authentication and authorization
- Multi-organization support
- Advanced reporting and analytics
- Payroll and salary management
- Leave management system
- Performance reviews
- Export to CSV/PDF
- Multi-language support
- Dark mode
- Mobile app (React Native)
- Email notifications
- Calendar view for attendance
- Integration with other HR tools

---

**Built with ❤️ for HR teams everywhere**

Last Updated: February 24, 2026
