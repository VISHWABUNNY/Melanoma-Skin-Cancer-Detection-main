from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    # Currently a dummy predict route.
    # In the future, the trained CNN model from Melanoma_SkinCancer_Detection.ipynb will be loaded here.
    return jsonify({"status": "success", "prediction": "Not Implemented", "message": "Backend successfully received the request!"})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "status": "online", 
        "message": "Melanoma Detection API is running. Send POST requests to /api/predict"
    })

if __name__ == '__main__':
    # Running on port 5050
    app.run(host='0.0.0.0', port=5050, debug=True)
