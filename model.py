import pickle

# Load the trained model
model_path = "model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

def predict_8th_sem(sem_marks):
    """
    Predicts 8th semester marks based on semesters 1 to 7 marks.
    
    Args:
        sem_marks (list): A list of 7 marks (sem1 to sem7).
        
    Returns:
        float: Predicted 8th semester marks.
    """
    if len(sem_marks) != 7:
        raise ValueError("Input must contain marks for exactly 7 semesters.")
    prediction = model.predict([sem_marks])  # Model expects a 2D array
    return prediction[0]
