text = input()
command = input()

while command != "Generate":
    splitted_command = command.split(">>>")
    f_command = splitted_command[0]
    if f_command == "Contains":
        substring = splitted_command[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")
    elif f_command == "Flip":
        s_command = splitted_command[1]
        start_index = int(splitted_command[2])
        end_index = int(splitted_command[3])

        if s_command == "Upper":
            first_part = text[:start_index]
            second_part = text[end_index:]
            upper_part = text[start_index:end_index]
            upper_part = upper_part.upper()
            text = first_part + upper_part + second_part

        elif s_command == "Lower":
            first_part = text[:start_index]
            second_part = text[end_index:]
            lower_part = text[start_index:end_index]
            lower_part = lower_part.lower()
            text = first_part + lower_part + second_part
        print(text)

    elif f_command == "Slice":
        start_index = int(splitted_command[1])
        end_index = int(splitted_command[2])
        first_part = text[:start_index]
        second_part = text[end_index:]
        text = first_part + second_part
        print(text)

    command = input()

print(f"Your activation key is: {text}")