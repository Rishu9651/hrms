# HRMS Frontend

React-based frontend for the Human Resource Management System (HRMS).

## Tech Stack

- Framework: React 18
- Build Tool: Vite
- Styling: Tailwind CSS
- HTTP Client: Axios
- Node: v18+, npm v10+

## Project Structure

```
hrms-frontend/
├── src/
│   ├── main.jsx              # Application entry point
│   ├── App.jsx               # Main app component
│   ├── index.css             # Global styles (Tailwind)
│   ├── api.js                # API client and endpoints
│   └── components/
│       ├── Header.jsx        # Header with navigation
│       ├── EmployeeList.jsx  # Employee list table
│       ├── EmployeeForm.jsx  # Add/edit employee modal
│       ├── AttendanceManagement.jsx  # Attendance management
│       ├── AttendanceForm.jsx        # Mark attendance modal
│       └── AttendanceRecords.jsx     # Attendance view with filters
├── index.html                # HTML entry point
├── package.json              # NPM dependencies
├── vite.config.js           # Vite configuration
├── tailwind.config.js       # Tailwind CSS configuration
├── postcss.config.js        # PostCSS configuration
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Installation and Setup

### Prerequisites
- Node.js v18+
- npm v10+

### Local Development

1. Install dependencies:
   ```bash
   npm install
   ```

2. Create .env file (copy from .env.example):
   ```bash
   cp .env.example .env
   ```
   
   Update the API URL if backend is on a different server:
   ```env
   VITE_API_URL=http://localhost:8000/api
   ```

3. Start development server:
   ```bash
   npm run dev
   ```
   
   The application will be available at http://localhost:3000

4. Build for production:
   ```bash
   npm run build
   ```
   
   Output will be in the dist/ directory

## Features

### Employee Management
- Add new employees with validation
- View all employees in a searchable table
- Edit employee details
- Delete employees with confirmation
- Search by name, ID, or email
- Error handling and validation messages

### Attendance Management
- Select employee and mark attendance
- View attendance records with filters
- Filter by status (Present/Absent)
- Sort attendance records by date
- View attendance statistics:
  - Total records
  - Days present
  - Days absent
- Delete attendance records

### UI Features
- Professional, responsive design
- Real-time error messages
- Success notifications
- Loading states
- Empty states with helpful messages
- Mobile-friendly layout
- Smooth animations and transitions
- Tabbed navigation (Employees/Attendance)

## API Integration

The frontend connects to the FastAPI backend via the /api prefix. All endpoints are defined in src/api.js:

```javascript
import { employeeAPI, attendanceAPI, statsAPI } from './api'

// Employee operations
employeeAPI.getAll()
employeeAPI.create(data)
employeeAPI.update(id, data)
employeeAPI.delete(id)

// Attendance operations
attendanceAPI.create(data)
attendanceAPI.getByEmployee(employeeId)
attendanceAPI.update(id, data)
attendanceAPI.delete(id)

// Statistics
statsAPI.getEmployeeCount()
statsAPI.getAttendanceSummary(employeeId)
```

## Environment Variables

Copy .env.example to .env and customize:

```env
# Backend API URL
VITE_API_URL=http://localhost:8000/api
```

## Build and Deployment

### Development Build
```bash
npm run dev
```

### Production Build
```bash
npm run build
```

### Preview Production Build Locally
```bash
npm run preview
```

### Deployment to Vercel

1. Push code to GitHub
2. Connect repository to Vercel
3. Set environment variables in Vercel dashboard:
   ```
   VITE_API_URL=https://your-backend-url.com/api
   ```
4. Deploy

Alternative: Deploy with Vercel CLI
```bash
npm i -g vercel
vercel
```

### Deployment to Netlify

1. Push code to GitHub
2. Connect repository to Netlify
3. Build command: npm run build
4. Publish directory: dist
5. Set environment variables
6. Deploy

## Component Overview

### Header
- Displays app title and slogan
- Shows total employee count
- Fetches stats from API

### EmployeeList
- Searchable employee table
- Edit and delete actions
- Loading and empty states
- Responsive design

### EmployeeForm
- Add/edit employee modal
- Validation (required fields, email format)
- Department selection dropdown
- Success/error handling

### AttendanceManagement
- Employee selector
- Button to mark attendance
- Attendance records display
- Statistics cards

### AttendanceForm
- Date picker (max date is today)
- Status selection (Present/Absent)
- Validation and error handling
- Submit and cancel actions

### AttendanceRecords
- Statistics cards (total, present, absent)
- Filter by status
- Sort by date
- Responsive table
- Delete functionality

## Error Handling

The app provides user-friendly error messages for:
- Network errors
- Validation errors
- Duplicate records
- Not found errors
- Server errors

All errors are displayed as toast notifications.

## Performance Considerations

- Components use React hooks for efficient state management
- API calls are cached when viewing records
- Minimal re-renders with proper dependency arrays
- Tailwind CSS for optimized styling
- Vite for fast development and optimized builds

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Notes

- Frontend assumes single admin user (no authentication)
- Search is case-insensitive
- Date picker prevents selecting future dates
- Attendance can only be marked once per employee per day
- All timestamps are stored as dates (YYYY-MM-DD format)
