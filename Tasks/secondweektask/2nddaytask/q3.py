## write your program here
num1 = input("Enter the first number: ")
num2 = input("Enter the Second  number: ")
num3 = input("Enter the third number: ")

if num1 > num2:
  if num1 > num3:
    print(f"max number: {num1}")
  else:
    print(f"max number: {num3}")


else:
  if num2 > num3:
    print(f"max number: {num2}")
  else:
    print(f"max number: {num3}")