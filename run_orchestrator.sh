#!/bin/bash
source venv/bin/activate

echo "🔄 Bootstrapping Back-end Engine Matrix on Port 8000..."
python3 backend/app/main.py &

echo "🔄 Initializing Client Front-end Dashboard Ecosystem..."
cd frontend
npm run dev &

# Keep script alive to manage child background execution tasks
wait
