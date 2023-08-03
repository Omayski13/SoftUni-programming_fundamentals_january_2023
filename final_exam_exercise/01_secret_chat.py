text = input()
command = input()

while command != "Reveal":
    splitted_command= command.split(":|:")
    f_command, s_command = splitted_command[0],splitted_command[1]
    if f_command == "InsertSpace":
        s_command = int(s_command)
        text = text[:s_command] + " " + text[s_command:]
    elif f_command == "Reverse":
        if s_command in text:
            text = text.replace(s_command,"",1)
            s_command = s_command[::-1]
            text = text + s_command
        else:
            print("error")
            command = input()
            continue

    if f_command == "ChangeAll":
        for i in range(1, (len(splitted_command))):
            replacement = splitted_command[i]
            text = text.replace(s_command, replacement,)

    command = input()
    print(text)

print(f"You have a new text message: {text}")