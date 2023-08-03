text = input()

command = input()
while command !="Done":
    if command == "TakeOdd":
        text_list = []
        counter = 0
        for el in text:
            if counter % 2 != 0:
                text_list.append(el)
            counter += 1
        text = "".join(text_list)
        print(text)

    else:
        f_command, s_command, t_command = command.split()
        if f_command == "Cut":
            s_command = int(s_command)
            t_command = int(t_command)
            text = text[:s_command] + text[s_command + t_command:]
            print(text)

        elif f_command == "Substitute":
            if s_command in text:
                text = text.replace(s_command, t_command)
            else:
                print("Nothing to replace!")
                command = input()
                continue
            print(text)


    command = input()

print(f"Your password is: {text}")