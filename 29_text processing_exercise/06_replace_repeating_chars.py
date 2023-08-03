word = input()
result = []
last_letter = ""

for letter in word:
    while letter != last_letter:
        result.append(letter)
        last_letter = letter

print("".join(result))



