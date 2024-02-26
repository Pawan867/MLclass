# # Task 03: Word Frequency Counter

# ## Objective
# Create a program that analyzes a given text and counts the frequency of each unique word.

# ## Requirements

# 1. Ask the user to input a paragraph or sentence.
# 2. Tokenize the input into words (ignoring punctuation and case sensitivity).
# 3. Count the frequency of each unique word.
# 4. Display the word frequencies in alphabetical order.
# 5. Handle cases where the input is empty.

import string


def count_words(text):
    if not text:
        print("Oops! You didn't provide any text.")
        return

    # Removing punctuation and converting to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    word_freq = {}

    # Counting word frequencies
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Displaying word frequencies
    for word, freq in sorted(word_freq.items()):
        print(f"{word}: {freq}")


if __name__ == "__main__":
    paragraph = input("Please type or paste some text: ")
    count_words(paragraph)
