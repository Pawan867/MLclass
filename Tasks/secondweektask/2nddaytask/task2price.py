def calculate_ticket_price(age_str, is_student):
    try:
        age = int(age_str)
        if age < 0:
            return "Age cannot be negative."
        if age <= 12:
            return "$10" if not is_student else "$8"
        elif age <= 17:
            return "$15" if not is_student else "$13"
        else:
            return "$20" if not is_student else "$18"
    except ValueError:
        return "Invalid age format. Please enter a valid non-negative integer age."


age_input = input("Enter your age: ")
is_student_input = input("Are you a student? (True/False): ").lower()
if is_student_input == 'true':
    is_student = True
else:
    is_student = False

ticket_price = calculate_ticket_price(age_input, is_student)
print(f"Ticket price: {ticket_price}")
