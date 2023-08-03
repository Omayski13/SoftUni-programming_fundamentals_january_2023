words = input().split()
counted_letters = {}
for word in words:
    for letter in word:
        if letter not in counted_letters:
            counted_letters[letter] = 1
        else:
            counted_letters[letter] += 1


for char,occurrences in counted_letters.items():
    print(f"{char} -> {occurrences}")