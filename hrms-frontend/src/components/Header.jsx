import { useState, useEffect } from 'react'
import { statsAPI } from '../api'

function Header() {
  const [employeeCount, setEmployeeCount] = useState(0)

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await statsAPI.getEmployeeCount()
        setEmployeeCount(response.data.total_employees)
      } catch (err) {
        console.error('Failed to load stats:', err)
      }
    }
    fetchStats()
  }, [])

  return (
    <header className="bg-blue-600 text-white shadow-lg">
      <div className="max-w-7xl mx-auto px-4 py-6">
        <h1 className="text-3xl font-bold">HRMS Lite</h1>
        <p className="text-blue-100 mt-1">Human Resource Management System</p>
        <div className="mt-4 text-sm">
          <span className="bg-blue-700 px-3 py-1 rounded-full">Total Employees: {employeeCount}</span>
        </div>
      </div>
    </header>
  )
}

export default Header
