# Q.7 Write a Python function that takes a number as a parameter and check the
# number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


number = 17
print(f"The number {number} is prime: {is_prime(number)}")
