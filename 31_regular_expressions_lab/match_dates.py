import re
text = input()

pattern = r"\b(?P<Day>\d{2})([-./])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})\b"

result = re.finditer(pattern, text)

for date in result:
    data_data = date.groupdict()
    print(f"Day: {data_data['Day']}, Month: {data_data['Month']}, Year: {data_data['Year']}")

