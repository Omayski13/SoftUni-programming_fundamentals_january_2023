import re

text = input()

pattern = r"(=|/)([A-Z][a-zA-Z]{2,})\1"

result = re.findall(pattern, text)
destinations = []
total_letters = 0

for i in result:
    destinations.append(i[1])

for destination in destinations:
    for letter in destination:
        total_letters += 1

print(f'Destinations: {", ".join(destinations)}')
print(f"Travel Points: {total_letters}")