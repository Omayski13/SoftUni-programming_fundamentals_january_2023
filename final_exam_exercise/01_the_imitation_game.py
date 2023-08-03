text = input()
command = input()

while command != "Decode":
    splitted_command = command.split("|")
    first_command = splitted_command[0]
    if first_command == "Move":
        num_of_letters = int(splitted_command[1])
        first_part = text[:num_of_letters]
        second_part = text[num_of_letters:]
        text = second_part + first_part
    elif first_command == "Insert":
        index = int(splitted_command[1])
        value = splitted_command[2]
        first_part = text[:index]
        second_part = text[index:]
        text = first_part + value + second_part
    elif first_command == "ChangeAll":
        substring = splitted_command[1]
        replacement = splitted_command[2]
        text = text.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {text}")