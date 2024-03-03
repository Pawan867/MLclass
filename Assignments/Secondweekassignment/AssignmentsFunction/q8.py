# Q.8 Write a python function to print the even numbers from a given list.
def even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    print("Even numbers in the list:", even_numbers)


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers(input_list)
