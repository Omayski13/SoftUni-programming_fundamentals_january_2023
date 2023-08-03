import re
text = input()

result = re.findall(r"\b_([a-zA-Z\d]+)\b", text)

print(",".join(result))
