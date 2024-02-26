def calculate_grade(score):
    if 0 <= score <= 100:
        if 90 <= score <= 100:
            return "A"
        elif 80 <= score < 90:
            return "B"
        elif 70 <= score < 80:
            return "C"
        elif 60 <= score < 70:
            return "D"
        else:
            return "F"
    else:
        return "Invalid score"


def main():
    while True:
        try:
            score = float(input("Enter score: "))
            if score < 0 or score > 100:
                raise ValueError
            grade = calculate_grade(score)
            print("Grade:", grade)
            break
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()
