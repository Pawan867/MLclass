def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score. Score must be between 00 and 100."
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


try:
    score = float(input("Enter the student's score: "))
    print("Grade:", calculate_grade(score))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
