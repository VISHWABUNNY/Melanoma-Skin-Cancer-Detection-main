#!/bin/bash

# Configuration
FRONTEND_DIR="frontend"
BACKEND_DIR="backend"

echo "======================================"
echo " Starting Melanoma Detection Project  "
echo "======================================"

# Clean up processes on Ctrl+C (SIGINT) or exit
cleanup() {
    echo ""
    echo "Shutting down services..."
    kill $(jobs -p) 2>/dev/null
    exit 0
}
trap cleanup SIGINT EXIT

# Function to setup and run a component
setup_and_run() {
    local dir=$1
    local port=$2
    local command=$3
    local name=$4

    echo "[INFO] Setting up $name in ./$dir"
    cd "$dir" || { echo "[ERROR] Directory $dir not found"; exit 1; }

    # Create virtual environment if it doesn't exist
    if [ ! -d ".venv" ]; then
        echo "[INFO] Creating virtual environment for $name..."
        python3 -m venv .venv
    fi

    # Activate venv
    source .venv/bin/activate
    
    # Install requirements
    echo "[INFO] Installing dependencies for $name..."
    pip install -r requirements.txt -q
    
    # Run the application
    echo "[INFO] Starting $name on port $port..."
    eval "$command" &
    
    cd ..
}

# 1. Start Backend (Flask)
setup_and_run "$BACKEND_DIR" "5050" "python3 app.py" "Backend"

sleep 2 # Give backend a moment to start

# 2. Start Frontend (Streamlit)
setup_and_run "$FRONTEND_DIR" "8501" "streamlit run app.py --server.port 8501 --server.headless true" "Frontend"

echo "======================================"
echo " Project is running!"
echo " Frontend: http://localhost:8501"
echo " Backend:  http://localhost:5050"
echo " Press Ctrl+C to stop both services."
echo "======================================"

sleep 3 # Give streamlit a moment to initialize
echo "[INFO] Opening frontend in your default browser..."
python3 -m webbrowser "http://localhost:8501" > /dev/null 2>&1 || xdg-open "http://localhost:8501" > /dev/null 2>&1 || true

# Wait for background processes to keep script running
wait
