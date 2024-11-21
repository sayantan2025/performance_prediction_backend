

from joblib import dump
from sklearn.linear_model import LinearRegression  # Replace with your actual model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

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
dump(model, 'model.joblib')  # Save to current directory
print("Model saved successfully!")
