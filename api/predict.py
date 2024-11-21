from flask import Flask, request, jsonify
from joblib import dump, load
from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split
import pandas as pd

app = Flask(__name__)

# Train and save the model (equivalent to create_model.py)
def train_and_save_model():
    data = pd.read_csv('Data.csv')

    # Drop the index column
    data = data.drop(columns=['Unnamed: 0'])

    # Define features (X) and target (y)
    X = data.drop(columns=['SEM-VIII'])
    y = data['SEM-VIII']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save the model using joblib
    dump(model, 'model.joblib')
    print("Model trained and saved as model.joblib")

# Load the model for prediction (equivalent to model.py)
def load_model():
    return load('model.joblib')

# Train the model once when the script is first executed
train_and_save_model()
model = load_model()

@app.route('/')
def home():
    return "Flask app is running!"

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
        
        # Prepare the input for prediction
        input_data = [[sem1, sem2, sem3, sem4, sem5, sem6, sem7]]
        
        # Make the prediction
        prediction = model.predict(input_data)
        
        # Return the prediction as a JSON response
        return jsonify({"predicted_8th_sem": prediction[0]})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
