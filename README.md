# JailbrokeGPT

An uncensored AI chat interface powered by Dolphin-2.9.4-Llama3.1-8B, built with Flask and React.

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

Currently using: **Dolphin-2.9.4-Llama3.1-8B** (GGUF format)
- Model: bartowski/dolphin-2.9.4-llama3.1-8b-GGUF (Q4_K_S quantization)
- Size: 4.69GB
- RAM Required: ~7-8GB
- CPU optimized via llama.cpp
- Uncensored fine-tune ideal for coding assistance

### Upgrading to Larger Models

When you upgrade your server RAM, you can swap models by editing `backend/.env`:

```env
MODEL_REPO=your-model-repo/model-name
MODEL_FILE=model-file.gguf
```

## Deployment

Instructions for deploying to your home server will be added after development is complete.

## License

MIT
