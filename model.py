
from joblib import load

# Load the model (only once when the Flask app starts)
model = load('model.joblib')

def predict_marks(sem1, sem2, sem3, sem4, sem5, sem6, sem7):
    input_data = [[sem1, sem2, sem3, sem4, sem5, sem6, sem7]]
    prediction = model.predict(input_data)
    return prediction[0]  # Return the predicted value
