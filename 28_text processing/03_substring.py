removing_word = input()
word = input()
result = word

while removing_word in result:
    result = result.replace(removing_word,"")


print(result)