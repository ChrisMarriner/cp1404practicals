"""
Christopher Marriner
CP1404 Practical
Word Occurrences program
"""

word_to_count = {}

string = input("Text: ")
words = string.split()
for word in words:
    key = word_to_count.get(word, 0)
    word_to_count[word] = key + 1
words = list(word_to_count.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))
