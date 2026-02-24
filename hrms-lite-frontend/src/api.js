import axios from 'axios'

// Use environment variable for API URL, fallback to localhost
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Employee API calls
export const employeeAPI = {
  getAll: () => api.get('/employees'),
  getById: (id) => api.get(`/employees/${id}`),
  create: (data) => api.post('/employees', data),
  update: (id, data) => api.put(`/employees/${id}`, data),
  delete: (id) => api.delete(`/employees/${id}`),
}

// Attendance API calls
export const attendanceAPI = {
  getAll: () => api.get('/attendance'),
  getByEmployee: (employeeId) => api.get(`/attendance/employee/${employeeId}`),
  create: (data) => api.post('/attendance', data),
  update: (id, data) => api.put(`/attendance/${id}`, data),
  delete: (id) => api.delete(`/attendance/${id}`),
}

// Stats API calls
export const statsAPI = {
  getEmployeeCount: () => api.get('/stats/employees/count'),
  getAttendanceSummary: (employeeId) => api.get(`/stats/employees/${employeeId}/attendance-summary`),
}

export default api
