"""
JailbrokeGPT Flask Backend
Main application entry point
"""
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from model_loader import ModelLoader

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Configuration
MODEL_REPO = os.getenv('MODEL_REPO', 'v8karlo/UNCENSORED-TinyLlama-1.1B-intermediate-step-1431k-3T-Q5_K_M-GGUF')
MODEL_FILE = os.getenv('MODEL_FILE', 'uncensored-tinyllama-1.1b-intermediate-step-1431k-3t-q5_k_m.gguf')
MAX_TOKENS = int(os.getenv('MAX_TOKENS', 512))
TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
TOP_P = float(os.getenv('TOP_P', 0.9))
FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))
FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')

# Initialize model loader
print("Initializing JailbrokeGPT...")
model_loader = ModelLoader(MODEL_REPO, MODEL_FILE)

# Load model on startup
try:
    model_loader.load_model()
except Exception as e:
    print(f"Error loading model: {e}")
    print("Server will start but model needs to be loaded manually")


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model_loader.model is not None
    })


@app.route('/chat', methods=['POST'])
def chat():
    """
    Main chat endpoint
    
    Expected JSON body:
    {
        "prompt": "Your message here",
        "max_tokens": 512,  # optional
        "temperature": 0.7  # optional
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'prompt' not in data:
            return jsonify({'error': 'Missing prompt in request body'}), 400
        
        prompt = data['prompt']
        max_tokens = data.get('max_tokens', MAX_TOKENS)
        temperature = data.get('temperature', TEMPERATURE)
        
        # Format prompt for chat
        formatted_prompt = f"User: {prompt}\nAssistant:"
        
        # Generate response
        response = model_loader.generate(
            prompt=formatted_prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=TOP_P
        )
        
        return jsonify({
            'response': response,
            'prompt': prompt
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/model-info', methods=['GET'])
def model_info():
    """Get information about the loaded model"""
    return jsonify({
        'model_repo': MODEL_REPO,
        'model_file': MODEL_FILE,
        'max_tokens': MAX_TOKENS,
        'temperature': TEMPERATURE,
        'top_p': TOP_P,
        'loaded': model_loader.model is not None
    })


if __name__ == '__main__':
    print(f"\n🚀 JailbrokeGPT Backend running on http://{FLASK_HOST}:{FLASK_PORT}")
    print(f"📦 Model: {MODEL_REPO}")
    print(f"💬 Chat endpoint: http://localhost:{FLASK_PORT}/chat")
    print("\nPress CTRL+C to stop the server\n")
    
    app.run(
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=True
    )
