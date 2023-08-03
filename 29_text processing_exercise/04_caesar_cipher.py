text = input()
cripted_text = []

for letter in text:
    new_letter = chr(ord(letter)+3)
    cripted_text.append(new_letter)

print("".join(cripted_text))
