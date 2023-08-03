import re

text = input()
pattern = r"(#|@)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
result = re.findall(pattern, text)

if not result:
    print("No word pairs found!")
else:
    print(f"{len(result)} word pairs found!")
mirror_words = []
for elements in result:
    if elements[1] == elements[2][::-1]:
        mirror_words.append(f"{elements[1]} <=> {elements[2]}")

if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(f", ".join(mirror_words))

