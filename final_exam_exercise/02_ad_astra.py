import re

text = input()

pattern = r'(#|\|)([A-Z a-z]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'

results = re.findall(pattern, text)

items = []
expary_dates = []
calories = []
for match in results:
    items.append(match[1])
    expary_dates.append(match[2])
    calories.append(int(match[3]))

print(f"You have food to last you for: {sum(calories) // 2000} days!")
for index in range(len(items)):
    print(f"Item: {items[index]}, Best before: {expary_dates[index]}, Nutrition: {calories[index]}")
