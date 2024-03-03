# Q.2 Write a python function to reverse a string
def reverse_string(s):
    return s[::-1]


original_string = input("Enter The string here: ")
reversed_string = reverse_string(original_string)
print(f"Original: {original_string}, Reversed: {reversed_string}")
