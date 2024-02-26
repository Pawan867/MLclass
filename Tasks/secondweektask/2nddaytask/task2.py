# Task 02: Ticket Price Calculator Exercise

# ## Objective
# Create a program that calculates the ticket price for a movie based on the age and whether the customer is a student.

# ## Requirements

# 1. Get the user's age and whether they are a student (True or False) as input.
# 2. Define the ticket prices:
#    - Children (age 0-12): \$10
#    - Teenagers (age 13-17): \$15
#    - Adults (age 18 and above): $20
#    - Students (regardless of age): \$18 (discounted price)
# 3. Calculate and print the ticket price based on the user's age and student status.
# 4. Handle cases where the entered age is not a valid numeric value.
# 5. Provide a message for cases where the age is negative or non-integer.
# def calclate_ticket_price(age, is_student):
#     if not isinstance(age, (int, float)):
#         return "Invalid entry! Please enter a number."
#     if age < 0 or not age.is_integer():
#         return "Invalid entry! Please enter a positive integer."
def calculate_ticket_price(age, is_student):
    try:
        age = int(age)
        if age < 0:
            print("Age cannot be negative.")
            return
    except ValueError:
        print("Please enter a valid age.")
        return

    ticket_prices = {12: 10, 17: 15, float('inf'): 20}
    ticket_price = next(
        price for limit, price in ticket_prices.items() if age <= limit)

    if is_student:
        ticket_price = 18

    print(f"The ticket price is ${ticket_price}.")


if __name__ == "__main__":
    age = input("How old are you? ")
    is_student = input("Are you a student? (yes/no): ").lower() == "yes"

    calculate_ticket_price(age, is_student)
