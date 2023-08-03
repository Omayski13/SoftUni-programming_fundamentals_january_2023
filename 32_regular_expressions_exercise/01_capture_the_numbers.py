import re
numbers = []
pattern = r"\d+"
line = input()
while True:
    if not line:
        break
    result = re.findall(pattern, line)
    numbers.extend(result)

    line = input()

print(" ".join(numbers))