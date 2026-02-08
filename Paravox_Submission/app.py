from flask import Flask, request, jsonify
import os

# Paravox Gemini Bridge Server
# This automated script acts as a middleware gateway for the Paravox Smart Glove.
# It receives sensor data from the ESP32 (via Android Bridge) and sends it to Gemini API.

app = Flask(__name__)

# Mock Environment Variable for API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE")

@app.route('/')
def home():
    return "Paravox AI Gateway is Running! 🚀"

@app.route('/process_gesture', methods=['POST'])
def process_gesture():
    """
    Receives gesture data (flex sensor values) and uses Gemini to generate speech.
    """
    data = request.json
    flex_values = data.get('sensors', [])
    
    if not flex_values:
        return jsonify({"error": "No sensor data received"}), 400

    # Logic to call Gemini API would go here
    # response = gemini.generate_content(f"Translate these sensor values: {flex_values}")
    
    # Mock Response for Testing
    mock_speech = "User is signaling for Help."
    print(f"Received: {flex_values} -> Generated: {mock_speech}")
    
    return jsonify({
        "status": "success",
        "speech_output": mock_speech,
        "ai_model": "Gemini 1.5 Flash"
    })

@app.route('/health_check', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "Paravox Guardian System"})

if __name__ == '__main__':
    print("Starting Paravox Server...")
    app.run(host='0.0.0.0', port=5000)
