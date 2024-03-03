# Q.6 Write a python function that takes a list and returns a new list with unique elements of the first list
def unique_elements(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list


input_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = unique_elements(input_list)
print(f"Original list: {input_list}\nUnique list: {unique_list}")
