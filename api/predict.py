# api/predict.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    # Perform prediction logic here
    predicted_marks = predict_8th_sem(sem_marks)  # Replace with your model's prediction logic
    return jsonify({"predicted_8th_sem": predicted_marks})

if __name__ == "__main__":
    app.run(debug=True)
