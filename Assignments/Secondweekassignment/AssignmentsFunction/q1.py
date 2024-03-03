# **`Q.1 Write a python function to multiply all the numbers in a list`**
def multiply_num_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


numbers = [2, 3, 4]
result = multiply_num_list(numbers)
print(f"The multiplication of {numbers} is {result}")
