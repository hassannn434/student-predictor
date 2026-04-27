# Student Performance Predictor
# Simple logic-based model using study hours and attendance

def predict_performance(study_hours, attendance):
    score = (study_hours * 5) + (attendance * 0.5)

    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Average"
        return "Needs Improvement"


# --- Main Program ---
print("=== Student Performance Predictor ===")

try:
    study_hours = float(input("Enter study hours per day: "))
    attendance = float(input("Enter attendance percentage: "))

    result = predict_performance(study_hours, attendance)

    print("\nPredicted Performance:", result)

except:
    print("Invalid input! Please enter numeric values.")