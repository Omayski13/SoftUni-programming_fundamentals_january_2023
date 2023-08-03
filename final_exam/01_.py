import re

password = input()
command = input()



while command != "Complete":
    if command == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        result_letter_digits_dolna_cherta = re.findall(r"\([a-zA-Z0-9_])",password)
        if not result_letter_digits_dolna_cherta:
            print("Password must consist only of letters, digits and _!")
        result_upper = re.findall(r"[A-Z]{1,}",password)
        if not result_upper:
            print("Password must consist at least one uppercase letter!")
        result_lower = re.findall(r"[a-z]{1,}",password)
        if not result_lower:
            print("Password must consist at least one lowercase letter!")
        result_digits = re.findall(r"\d",password)
        if not result_digits:
            print("Password must consist at least one digit!")

    else:
        f_command, s_command, t_command = command.split()
        if f_command == "Make":
            if s_command == "Upper":
                t_command = int(t_command)
                password = password[:t_command] + password[t_command].upper() + password[t_command+1:]
                print(password)
            elif s_command == "Lower":
                t_command = int(t_command)
                password = password[:t_command] + password[t_command].lower() + password[t_command + 1:]
                print(password)
        elif f_command == "Insert":
            s_command = int(s_command)
            if 0 <= s_command <= len(password):
                password = password[:s_command] + t_command + password[s_command:]
                print(password)
        elif f_command == "Replace":
            char = s_command
            value = int(t_command)
            new_char = chr(ord(char) + value)
            if char in password:
                password = password.replace(char,new_char)
                print(password)


    command = input()
