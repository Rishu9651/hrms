@echo off
REM HRMS Lite - Quick Start Script for Windows

setlocal enabledelayedexpansion

cls
echo.
echo ====================================================
echo         HRMS Lite - Starting Application
echo ====================================================
echo.

REM Check if we're in the right directory
if not exist "hrms-lite-backend" (
    echo Error: Please run this script from the HRMS Lite project root directory
    pause
    exit /b 1
)

if not exist "hrms-lite-frontend" (
    echo Error: Please run this script from the HRMS Lite project root directory
    pause
    exit /b 1
)

REM Start Backend
echo Starting Backend Server...
cd hrms-lite-backend

REM Check if venv exists
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
)

REM Activate venv and start backend
call venv\Scripts\activate.bat
pip install -r requirements.txt >nul 2>&1
start "HRMS Backend" python main.py

echo Backend started!
echo   API URL: http://localhost:8000
echo   Docs: http://localhost:8000/docs
echo.

REM Wait for backend to start
timeout /t 2 /nobreak

REM Start Frontend
echo Starting Frontend Server...
cd ..\hrms-lite-frontend

REM Install dependencies if needed
if not exist "node_modules" (
    echo Installing frontend dependencies...
    call npm install
)

REM Start frontend
start "HRMS Frontend" npm run dev

echo Frontend started!
echo   App URL: http://localhost:3000
echo.

echo.
echo ====================================================
echo           HRMS Lite is Running!
echo ====================================================
echo Frontend:  http://localhost:3000
echo Backend:   http://localhost:8000
echo API Docs:  http://localhost:8000/docs
echo ====================================================
echo.
echo Note: You can close this window, but leave the other
echo       two windows open (Backend and Frontend).
echo.
pause
