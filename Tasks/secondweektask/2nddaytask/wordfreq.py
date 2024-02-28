import string


def word_frequency_counter(text):

    word_freq = {}
    for word in text.lower().split():
        word = word.strip(string.punctuation)
        if word:
            word_freq[word] = word_freq.get(word, 0)+1
    for word in sorted(word_freq):
        print(f"{word}:{word_freq[word]}")


try:
    text = input("Enter The pragraph")
    word_frequency_counter(text)
except EOFError:
    print("NO Input Provided")
