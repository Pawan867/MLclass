def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid Input please enter betyween 0 to 100"
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
    score = int(input("Enter your Score :"))
    print(calculate_grade(score))
except ValueError:
    print("Enter the numeric value")
