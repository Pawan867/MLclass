
# Input from the user: operation, and two numbers
print("Calculator")
operation = input("Choose an operation (+, -, *, /): ")
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

# Perform the calculation based on the operation
if operation == '+':
    result = first + second
    print(f"{first} + {second} = {result}")
elif operation == '-':
    result = first - second
    print(f"{first} - {second} = {result}")
elif operation == '*':
    result = first * second
    print(f"{first} * {second} = {result}")
elif operation == '/':
    # Check to prevent division by zero
    if second != 0:
        result = first / second
        print(f"{first} / {second} = {result}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operation selected.")
