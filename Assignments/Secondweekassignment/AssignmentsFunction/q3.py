# Q.3 Write a python function to find factorial of a given non negativenumber
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


number = int(input("Enter a number : "))
fact = factorial(number)
print(f"The factorial of {number} is {fact}")
