def can_form_palindrome(s):
    s = s.replace(" ", "").lower()
    char_count = {}
    for char in s:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    odd_count = sum(count % 2 != 0 for count in char_count.values())
    return odd_count <= 1


try:
    user_input = input("Enter a string: ")
    if not user_input.strip():
        print("No input provided.")
    elif can_form_palindrome(user_input):
        print("The given string can be rearranged to form a palindrome.")
    else:
        print("The given string cannot be rearranged to form a palindrome.")
except Exception as e:
    print("An error occurred:", e)
