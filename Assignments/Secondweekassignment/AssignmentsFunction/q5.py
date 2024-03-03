# Q.5 Write a python function that accepts a string and calculate the number of upper case letters and lower case letters
def count_case_types(s):
    uppercase_count = sum(1 for char in s if char.isupper())
    lowercase_count = sum(1 for char in s if char.islower())
    return uppercase_count, lowercase_count


input_string = input("Enter  a string: ")
uppercase_count, lowercase_count = count_case_types(input_string)
print(
    f"In the string '{input_string}':\nUppercase letters: {uppercase_count}, Lowercase letters: {lowercase_count}")
