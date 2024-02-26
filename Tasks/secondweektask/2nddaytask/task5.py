# # Task 05: Palindromic Anagram Checker

# ## Objective
# Create a program that checks if a given string can be rearranged to form a palindromic string.

# ## Requirements

# 1. A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward.
# 2. Ask the user to input a string.
# 3. Check and print whether the given string can be rearranged to form a palindrome.
# 4. Ignore spaces and consider the characters in a case-insensitive manner.
# 5. Handle cases where the input is empty or contains non-alphabetic characters.

def is_palindromic_anagram(s):
    s = ''.join(c.lower() for c in s if c.isalpha())

    if not s:
        print("Please enter a non-empty string with alphabetic characters only.")
        return False

    odd_count = sum(s.count(c) % 2 for c in set(s))

    if odd_count <= 1:
        print("Yes, the given string can be rearranged to form a palindrome.")
    else:
        print("No, the given string cannot be rearranged to form a palindrome.")


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    is_palindromic_anagram(user_input)
