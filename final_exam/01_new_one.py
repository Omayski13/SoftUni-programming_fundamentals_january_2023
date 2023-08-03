import re

password = input()

command = input()

while command != "Complete":
    if command == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        result_l_d_more = re.findall(r"[A-Za-z0-9_],",password)
        if not result_l_d_more:
            print(o	"Password must consist only of letters, digits and _!")
    else:
        f_command, s_command, t_command = command.split()
        if f_command == "Make":
            index = int(t_command)
            if 0 <= index <= len(password):
                if s_command == "Upper":
                    password = password[:index] + password[index].upper() + password [index+1:]
                    print(password)
                elif s_command == "Lower":
                    password = password[:index] + password[index].lower() + password[index + 1:]
                    print(password)

        elif f_command == "Insert":
            index = int(s_command)
            char = t_command
            if 0 <= index <= len(password):
                password = password[:index] + char + password[index:]
                print(password)

        elif f_command == "Replace":
            char = s_command
            value = int(t_command)
            not_named = ord(char) + value
            new_symbol = chr(not_named)
            if char in password:
                password = password.replace(char, new_symbol)
                print(password)
            pass

    command = input()