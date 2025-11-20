#!/bin/bash

# LookMate Quick Start Script
# This script sets up and runs the LookMate application

echo "=========================================="
echo "  LookMate - AI Style Partner"
echo "=========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "myenv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv myenv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source myenv/bin/activate 2>/dev/null || source myenv/Scripts/activate 2>/dev/null

# Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

# Check if models exist
if [ ! -f "model/men.keras" ] || [ ! -f "model/Female.h5" ]; then
    echo "⚠️  Warning: ML models not found in model/ directory"
    echo "   Place men.keras and Female.h5 in the model/ directory"
fi

# Check if AR overlays exist
overlay_count=$(find assests -name "*.png" 2>/dev/null | wc -l)
if [ "$overlay_count" -lt 5 ]; then
    echo "Generating placeholder AR overlays..."
    python3 generate_placeholders.py
fi

echo ""
echo "=========================================="
echo "  Starting LookMate Application..."
echo "=========================================="
echo ""
echo "The app will open in your browser at:"
echo "  http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

# Run Streamlit app
streamlit run app.py
