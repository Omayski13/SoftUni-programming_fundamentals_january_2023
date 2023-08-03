text = input()
command = input()

while command != 'Travel':
    splitted_command = command.split(":")
    f_command = splitted_command[0]
    if f_command == "Add Stop":
        index = int(splitted_command[1])
        string = splitted_command[2]
        if 0 <= index < len(text):
            text = text[:index] + string + text[index:]
    elif f_command == "Remove Stop":
        start_index = int(splitted_command[1])
        end_index = int(splitted_command[2])
        if 0 <= start_index <= end_index < len(text):
            text = text[:start_index] + text[end_index + 1:]
    elif f_command == "Switch":
        old_string = splitted_command[1]
        new_string = splitted_command[2]
        if old_string in text:
            text = text.replace(old_string,new_string)
    print(text)
    command = input()

print(f"Ready for world tour! Planned stops: {text}")