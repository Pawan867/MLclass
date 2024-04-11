
class ageerror(Exception):
    "the input value is less than 20"
    pass


try:
    input_num = int(input("Enter a number: "))
    if input_num <= 30 and input_num > 20:
        raise ageerror
    else:
        print("Age is Ok")

except ageerror:
    print("Exception occurred: Invalid Age")
