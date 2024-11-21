# api/predict.py

import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model when the app starts
model = None

def load_model():
    global model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

@app.route('/api/predict', methods=['POST'])
def predict():
    if model is None:
        load_model()  # Load model if it's not already loaded
    
    # Get the data from the request
    data = request.json
    sem1 = data['sem1']
    sem2 = data['sem2']
    sem3 = data['sem3']
    sem4 = data['sem4']
    sem5 = data['sem5']
    sem6 = data['sem6']
    sem7 = data['sem7']
    
    # Prepare the input data
    input_data = [[sem1, sem2, sem3, sem4, sem5, sem6, sem7]]
    
    # Make prediction using the loaded model
    prediction = model.predict(input_data)
    
    # Return the prediction as JSON
    return jsonify({"predicted_8th_sem": prediction[0]})

# Vercel's serverless functions handle requests automatically, so no need for app.run()

if __name__ == "__main__":
    app.run(debug=True)
