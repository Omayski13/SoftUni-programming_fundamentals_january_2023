data = input()
strength = 0
new_text = ''

for index in range(len(data)):
    if strength > 0 and data[index] != '>':
        strength -= 1

    elif data[index] == '>':
        new_text += data[index]
        strength += int(data[index + 1])
    else:
        new_text += data[index]
print(new_text)