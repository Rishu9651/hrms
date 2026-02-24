#!/bin/bash

# HRMS Lite - Quick Start Script
# Starts both backend and frontend servers

echo "╔════════════════════════════════════════════════════╗"
echo "║         HRMS Lite - Starting Application           ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if we're in the right directory
if [ ! -d "hrms-lite-backend" ] || [ ! -d "hrms-lite-frontend" ]; then
    echo -e "${YELLOW}Error: Please run this script from the HRMS Lite project root directory${NC}"
    exit 1
fi

# Function to cleanup on exit
cleanup() {
    echo -e "\n${YELLOW}Shutting down servers...${NC}"
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

trap cleanup SIGINT

# Start Backend
echo -e "${BLUE}Starting Backend Server...${NC}"
cd hrms-lite-backend

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install dependencies if needed
if [ ! -f "venv_installed" ]; then
    echo "Installing backend dependencies..."
    pip install -r requirements.txt
    touch venv_installed
fi

# Start backend
python main.py &
BACKEND_PID=$!
echo -e "${GREEN}✓ Backend started (PID: $BACKEND_PID)${NC}"
echo -e "  ${BLUE}API URL: http://localhost:8000${NC}"
echo -e "  ${BLUE}Docs: http://localhost:8000/docs${NC}"

# Wait a moment for backend to start
sleep 2

# Start Frontend
echo ""
echo -e "${BLUE}Starting Frontend Server...${NC}"
cd ../hrms-lite-frontend

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
fi

# Start frontend
npm run dev &
FRONTEND_PID=$!
echo -e "${GREEN}✓ Frontend started (PID: $FRONTEND_PID)${NC}"
echo -e "  ${BLUE}App URL: http://localhost:3000${NC}"

echo ""
echo "╔════════════════════════════════════════════════════╗"
echo -e "║          ${GREEN}HRMS Lite is Running!${NC}             ║"
echo "╠════════════════════════════════════════════════════╣"
echo -e "║ Frontend:  ${GREEN}http://localhost:3000${NC}          ║"
echo -e "║ Backend:   ${GREEN}http://localhost:8000${NC}          ║"
echo -e "║ API Docs:  ${GREEN}http://localhost:8000/docs${NC}   ║"
echo "╠════════════════════════════════════════════════════╣"
echo "║ Press Ctrl+C to stop all servers                  ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Wait for processes to finish
wait
