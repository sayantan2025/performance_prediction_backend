from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict_8th_sem

app = Flask(__name__)
CORS(app)  # Allow CORS for local testing
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask App!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse incoming JSON data
        data = request.json
        sem_marks = [
            data["sem1"], data["sem2"], data["sem3"],
            data["sem4"], data["sem5"], data["sem6"], data["sem7"]
        ]
        prediction = predict_8th_sem(sem_marks)
        return jsonify({"predicted_8th_sem": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
