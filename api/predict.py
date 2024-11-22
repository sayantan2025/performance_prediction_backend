from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)

# Load the pre-trained model
try:
    model = load('model.joblib')
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Error: model.joblib file not found. Ensure the file exists in the deployment directory.")

@app.route('/')
def home():
    return "Flask app is running!"

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        data = request.json
        required_keys = ['sem1', 'sem2', 'sem3', 'sem4', 'sem5', 'sem6', 'sem7']

        # Validate input keys
        if not all(key in data for key in required_keys):
            return jsonify({"error": "Missing one or more required keys: sem1, sem2, sem3, sem4, sem5, sem6, sem7"}), 400

        # Extract features
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
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
