from flask import Flask, request, jsonify
from joblib import load
import os

app = Flask(__name__)

# Load the model at the start when the app starts
model = None
try:
    model = load('model.joblib')  # Make sure the model is loaded at startup
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    return "Flask app is running!"

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return jsonify({"error": "Model is not loaded"})
        
        # Get the input data from the request
        data = request.json
        sem1 = data['sem1']
        sem2 = data['sem2']
        sem3 = data['sem3']
        sem4 = data['sem4']
        sem5 = data['sem5']
        sem6 = data['sem6']
        sem7 = data['sem7']
        
        # Prepare the input for prediction
        input_data = [[sem1, sem2, sem3, sem4, sem5, sem6, sem7]]
        
        # Make the prediction
        prediction = model.predict(input_data)
        
        # Return the prediction as a JSON response
        return jsonify({"predicted_8th_sem": prediction[0]})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10000)
