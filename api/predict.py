# /api/predict.py

import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define the model and prediction logic here
def predict_marks(data):
    # Here you would load your model and make a prediction based on input data
    # This is just a placeholder logic
    return sum(data.values()) / len(data)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        prediction = predict_marks(data)
        return json.dumps({"predicted_8th_sem": prediction})
    except Exception as e:
        return json.dumps({"error": str(e)}), 400

# Vercel serverless function entry point
def handler(request):
    return app(request)
