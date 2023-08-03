num_of_lines = int(input())
dict = {}
for words in range (num_of_lines):
    word = input()
    synonym = input()
    if word not in dict:
        dict[word] = []
    dict[word].append(synonym)
for word in dict.keys():
    print(f'{word} - {", ".join(dict[word])}')

