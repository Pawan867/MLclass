
class ageerror(Exception):
    "The input value is less than 20"
    pass


number = 20
try:
    input_num = int(input("Enter a age: "))
    if input_num < number:
        raise ageerror
    else:
        print("Age is Ok")
except ageerror:
    print("Invalid Age")
