banned_word = input().split(", ")
text = input()

for word in banned_word:
    while word in text:
       text = text.replace(word,"*" * len(word))

print(text)