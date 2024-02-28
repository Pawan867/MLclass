def ticket_price_calculator(age_Str, is_student):

    try:
        age = int(age_Str)
        if age < 0:
            return"Age is not a negative"
        if age <= 12:
            return "$10" if not is_student else "$8"
        elif age <= 17:
            return "$15" if not is_student else "$13"

        else:
            return "$20" if not is_student else "$18"
    except ValueError:
        return "Invalid input. Please enter numeric value for age."


age_input = input("Enter The age: ")
is_student_input = input("Are yo a stident? (true/false)").lower()
if is_student_input == 'true':
    is_student = True
else:
    is_student = False
price_calculator = ticket_price_calculator(age_input, is_student)
print(f"Price Calculator{price_calculator}")
