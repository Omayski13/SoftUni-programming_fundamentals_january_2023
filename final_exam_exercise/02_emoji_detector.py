import re

text = input()

pattern = r'(\*\*|\:\:)([A-Z][a-z]{2,})\1'
emojis = re.findall(pattern, text)
matches = re.findall(r"\d", text)

dict_emojies = {}

for emoji in emojis:
    key_emoji = emoji[1]
    value_emoji = emoji[0]
    dict_emojies[key_emoji] = value_emoji

# print(emojis)

cool_treshold = 1

for match in matches:
    match = int(match)
    cool_treshold *= match


print(f"Cool threshold: {cool_treshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")

for key,value in dict_emojies.items():
    emoji_coolnest = 0
    for key_num in key:
        emoji_coolnest += ord(key_num)
    emoji_string = ""
    if emoji_coolnest > cool_treshold:
        emoji_string = str(dict_emojies[key]) + str(key) + str(dict_emojies[key])
        print(emoji_string)
    emoji_coolnest = 0

#
# print(f"Cool threshold: {cool_treshold}")
# print(f"{len(emojis)} emojis found in the text. The cool ones are:")
# emoji_coolnest = 0
# counter = 0
# for emoji in emojis:
#     if counter % 2 == 0:
#         counter += 1
#         continue
#     for letter in emoji:
#         emoji_coolnest += ord(letter)
#         if emoji_coolnest > cool_treshold:
#             print()
#
#
#     emoji_coolnest = 0
#     counter += 1