words = input().split()
result = []

for word in words:
    new_word = word * (len(word))
    result.append(new_word)

print("".join(result))