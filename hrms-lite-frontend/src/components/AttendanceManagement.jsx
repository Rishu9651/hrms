import { useState, useEffect } from 'react'
import { attendanceAPI } from '../api'
import AttendanceRecords from './AttendanceRecords'
import AttendanceForm from './AttendanceForm'

function AttendanceManagement({ employees, onSuccess, onError }) {
  const [selectedEmployee, setSelectedEmployee] = useState(null)
  const [attendanceRecords, setAttendanceRecords] = useState([])
  const [loading, setLoading] = useState(false)
  const [showForm, setShowForm] = useState(false)

  const fetchAttendance = async (employeeId) => {
    if (!employeeId) return
    
    setLoading(true)
    try {
      const response = await attendanceAPI.getByEmployee(employeeId)
      setAttendanceRecords(response.data)
    } catch (err) {
      onError('Failed to load attendance records')
    } finally {
      setLoading(false)
    }
  }

  const handleSelectEmployee = (e) => {
    const employeeId = parseInt(e.target.value)
    setSelectedEmployee(employeeId)
    if (employeeId) {
      fetchAttendance(employeeId)
    } else {
      setAttendanceRecords([])
    }
    setShowForm(false)
  }

  const handleAddAttendance = () => {
    if (selectedEmployee) {
      setShowForm(true)
    } else {
      onError('Please select an employee first')
    }
  }

  const handleAttendanceSubmit = async () => {
    if (selectedEmployee) {
      await fetchAttendance(selectedEmployee)
      setShowForm(false)
      onSuccess()
    }
  }

  const handleDeleteAttendance = async (attendanceId) => {
    if (window.confirm('Are you sure you want to delete this attendance record?')) {
      try {
        await attendanceAPI.delete(attendanceId)
        if (selectedEmployee) {
          await fetchAttendance(selectedEmployee)
        }
        onSuccess()
      } catch (err) {
        onError('Failed to delete attendance record')
      }
    }
  }

  return (
    <div>
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Attendance Management</h2>

      {/* Employee Selection */}
      <div className="bg-white rounded-lg shadow p-6 mb-6">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Select Employee
        </label>
        <select
          value={selectedEmployee || ''}
          onChange={handleSelectEmployee}
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
        >
          <option value="">-- Choose an employee --</option>
          {employees.map(emp => (
            <option key={emp.id} value={emp.id}>
              {emp.employee_id} - {emp.name}
            </option>
          ))}
        </select>
      </div>

      {/* Add Attendance Button */}
      {selectedEmployee && (
        <div className="mb-6">
          <button
            onClick={handleAddAttendance}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors font-medium"
          >
            + Mark Attendance
          </button>
        </div>
      )}

      {/* Attendance Form Modal */}
      {showForm && selectedEmployee && (
        <AttendanceForm
          employeeId={selectedEmployee}
          onCancel={() => setShowForm(false)}
          onSubmit={handleAttendanceSubmit}
        />
      )}

      {/* Attendance Records */}
      {selectedEmployee && (
        <AttendanceRecords
          records={attendanceRecords}
          loading={loading}
          employeeName={employees.find(e => e.id === selectedEmployee)?.name}
          onDelete={handleDeleteAttendance}
        />
      )}
    </div>
  )
}

export default AttendanceManagement
