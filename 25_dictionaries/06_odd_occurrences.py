words = input().lower().split()
dict = {}

for word in words:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1


for word, repeats in dict.items():
    if repeats % 2 != 0:
        print(word, end=' ')