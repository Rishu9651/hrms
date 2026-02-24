import { useState, useEffect } from 'react'
import Header from './components/Header'
import EmployeeList from './components/EmployeeList'
import EmployeeForm from './components/EmployeeForm'
import AttendanceManagement from './components/AttendanceManagement'
import './App.css'

function App() {
  const [activeTab, setActiveTab] = useState('employees')
  const [showForm, setShowForm] = useState(false)
  const [employees, setEmployees] = useState([])
  const [editingEmployee, setEditingEmployee] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [successMessage, setSuccessMessage] = useState('')

  const showSuccessMessage = (message) => {
    setSuccessMessage(message)
    setTimeout(() => setSuccessMessage(''), 3000)
  }

  const showErrorMessage = (message) => {
    setError(message)
    setTimeout(() => setError(''), 3000)
  }

  const refreshEmployees = async () => {
    setLoading(true)
    try {
      const { employeeAPI } = await import('./api')
      const response = await employeeAPI.getAll()
      setEmployees(response.data)
    } catch (err) {
      showErrorMessage('Failed to load employees: ' + (err.response?.data?.detail || err.message))
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    refreshEmployees()
  }, [])

  const handleAddEmployee = () => {
    setEditingEmployee(null)
    setShowForm(true)
  }

  const handleCloseForm = () => {
    setShowForm(false)
    setEditingEmployee(null)
  }

  const handleEmployeeFormSubmit = async () => {
    await refreshEmployees()
    handleCloseForm()
    showSuccessMessage(editingEmployee ? 'Employee updated successfully!' : 'Employee added successfully!')
  }

  const handleDeleteEmployee = async (employeeId) => {
    if (window.confirm('Are you sure you want to delete this employee?')) {
      try {
        const { employeeAPI } = await import('./api')
        await employeeAPI.delete(employeeId)
        await refreshEmployees()
        showSuccessMessage('Employee deleted successfully!')
      } catch (err) {
        showErrorMessage('Failed to delete employee: ' + (err.response?.data?.detail || err.message))
      }
    }
  }

  const handleEditEmployee = (employee) => {
    setEditingEmployee(employee)
    setShowForm(true)
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      
      {/* Messages */}
      {successMessage && (
        <div className="bg-green-500 text-white px-4 py-3 rounded-md m-4">
          {successMessage}
        </div>
      )}
      {error && (
        <div className="bg-red-500 text-white px-4 py-3 rounded-md m-4">
          {error}
        </div>
      )}

      <div className="max-w-7xl mx-auto p-4">
        {/* Tabs */}
        <div className="flex gap-4 mb-6 border-b">
          <button
            onClick={() => setActiveTab('employees')}
            className={`px-4 py-2 font-medium transition-colors ${
              activeTab === 'employees'
                ? 'border-b-2 border-blue-600 text-blue-600'
                : 'text-gray-600 hover:text-gray-800'
            }`}
          >
            Employees
          </button>
          <button
            onClick={() => setActiveTab('attendance')}
            className={`px-4 py-2 font-medium transition-colors ${
              activeTab === 'attendance'
                ? 'border-b-2 border-blue-600 text-blue-600'
                : 'text-gray-600 hover:text-gray-800'
            }`}
          >
            Attendance
          </button>
        </div>

        {/* Content */}
        {activeTab === 'employees' && (
          <div>
            <div className="mb-6 flex justify-between items-center">
              <h2 className="text-2xl font-bold text-gray-900">Employee Management</h2>
              <button
                onClick={handleAddEmployee}
                className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors font-medium"
              >
                + Add Employee
              </button>
            </div>

            {showForm && (
              <EmployeeForm
                employee={editingEmployee}
                onCancel={handleCloseForm}
                onSubmit={handleEmployeeFormSubmit}
              />
            )}

            <EmployeeList
              employees={employees}
              loading={loading}
              onEdit={handleEditEmployee}
              onDelete={handleDeleteEmployee}
            />
          </div>
        )}

        {activeTab === 'attendance' && (
          <AttendanceManagement
            employees={employees}
            onSuccess={() => showSuccessMessage('Attendance updated successfully!')}
            onError={(msg) => showErrorMessage(msg)}
          />
        )}
      </div>
    </div>
  )
}

export default App
