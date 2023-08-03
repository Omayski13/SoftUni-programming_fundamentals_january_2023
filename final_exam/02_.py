import re

pattern = r"^(.+)>(\d+|[a-z]|[A-Z]|[^<>]{1,})\<\1$"

num_of_lines = int(input())
for n in range(num_of_lines):
    password_list = []
    password = input()
    result = re.findall(pattern, password)
    if not result:
        print("Try another password!")
    else:
        for i in result:
            password_list.append(i[1])
            password_list = "".join(password_list)
            password_list = password_list.replace("|","")
        print(f'Password: {"".join(password_list)}')
