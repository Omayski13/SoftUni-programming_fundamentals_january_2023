import re

pattern = r"^(.+)\>(\d+)\|([a-z]{1,})\|([A-Z]{1,})\|([^<>]{1,})\<\1$"

num_of_lines = int(input())
for n in range(num_of_lines):
    pass_list = []
    password = input()
    result = re.findall(pattern, password)

    if not result:
        print("Try another password!")
    else:
        for el in result:
            pass_list.append(el[1])
            pass_list.append(el[2])
            pass_list.append(el[3])
            pass_list.append(el[4])

        print(f'Password: {"".join(pass_list)}')