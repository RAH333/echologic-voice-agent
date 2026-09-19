#!/bin/bash
set -e
echo "Running Automation Matrix Phase [1/4] - Global Setup Checks..."
curl -s http://localhost:8000/api/healthz | grep -q "ONLINE" && echo "Backend Service Reachable" || echo "Service Offline"
