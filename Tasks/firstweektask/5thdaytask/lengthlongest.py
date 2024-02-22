sample_list = ['mango', 'banana', 'kiwi', 'apple', 'grapes']
longest_word = sample_list[0]
longest_len = len(sample_list[0])
for word in sample_list:
    if len(word) > longest_len:
        longest_word = word
        longest_len = len(word)
print(longest_word, longest_len)
