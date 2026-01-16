# JailbrokeGPT

An uncensored AI chat interface powered by TinyLlama, built with Flask and React.

## Tech Stack

**Backend:**
- Python 3.9+
- Flask
- llama-cpp-python (PyTorch integration)
- Flask-CORS

**Frontend:**
- React 18
- TypeScript
- Vite
- Tailwind CSS

## Project Structure

```
jailbrokegpt/
├── backend/          # Flask API server
├── frontend/         # React frontend
└── README.md
```

## Setup Instructions

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the server:
```bash
python app.py
```

Backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run development server:
```bash
npm run dev
```

Frontend will run on `http://localhost:5173`

## Model Information

Currently using: **UNCENSORED-TinyLlama-1.1B** (GGUF format)
- Model: v8karlo/UNCENSORED-TinyLlama-1.1B-intermediate-step-1431k-3T-Q5_K_M-GGUF
- Size: ~1.5GB
- RAM Required: 2-3GB
- CPU optimized via llama.cpp

### Upgrading to Larger Models

When you upgrade your server RAM to 16GB, simply change the model name in `backend/.env`:

```
MODEL_NAME=darkc0de/XortronCriminalComputingConfig
```

## Deployment

Instructions for deploying to your home server will be added after development is complete.

## License

MIT
