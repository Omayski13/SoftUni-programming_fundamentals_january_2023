sentence = input()

for index in range(len(sentence)):
    if sentence[index] == ':' and len(sentence) - 1 != ':':
        print(f':{sentence[index + 1]}')