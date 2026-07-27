def get_long_words(words, min_length):
    long_words = []
    for word in words:
        if len(word) >= min_length:
            long_words.append(word)
    return long_words
text = input("Enter a sentence: ")
while not text:
    text = input("Please enter a non-empty sentence: ")
words = text.split()
print(words)
print(f"Number of words: {len(words)}")
upper_words = []
for word in words:
    print(word.upper())
    upper_words.append(word.upper())
print(upper_words)
min_length = int(input("Enter the minimum length of words to filter: "))
long_words = get_long_words(words, min_length)
print(long_words)
for position, word in enumerate(words, start=1):
    print(f"{position}: {word}")