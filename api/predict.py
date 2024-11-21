

from flask import Flask, request, jsonify
from model import predict_marks  # Importing the prediction function from model.py

app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        data = request.json
        sem1 = data['sem1']
        sem2 = data['sem2']
        sem3 = data['sem3']
        sem4 = data['sem4']
        sem5 = data['sem5']
        sem6 = data['sem6']
        sem7 = data['sem7']
        
        # Call the predict function from model.py
        prediction = predict_marks(sem1, sem2, sem3, sem4, sem5, sem6, sem7)
        
        # Return the prediction as a JSON response
        return jsonify({"predicted_8th_sem": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
