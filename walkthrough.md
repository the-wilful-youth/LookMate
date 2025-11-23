# LookMate Migration Walkthrough

I have successfully converted the LookMate application from Streamlit to a modern React + FastAPI architecture.

## 🚀 How to Run

You will need two terminal windows to run the application (one for backend, one for frontend).

### 1. Start the Backend (FastAPI)
This serves the API and static assets.

```bash
cd backend
# Install requirements if not already installed
pip install -r requirements.txt
# Run the server
uvicorn main:app --reload --port 8000
```

### 2. Start the Frontend (React)
This runs the user interface.

```bash
cd frontend
# Install dependencies if not already installed
npm install
# Run the dev server
npm run dev
```

Open your browser to the URL shown (usually `http://localhost:5173`).

## ✨ Features Implemented
- **Premium UI**: Dark mode, glassmorphism effects, and smooth transitions.
- **Dual Input**: Support for File Upload and Webcam capture.
- **Face Analysis**: Detects face shape and provides detailed characteristics.
- **Recommendations**: Displays tailored hairstyle and beard/makeup advice.
- **Asset Integration**: Dynamically loads style images from the backend.

## 📁 Project Structure
- `backend/`: Contains FastAPI app (`main.py`) and core logic (`face_shape_detector.py`, etc.).
- `frontend/`: Contains React app (Vite), components, and styles.
