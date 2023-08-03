my_list = [el for el in input().split(', ')]
command = input()
lost_names = 0
blacklisted_names = 0
while command != 'Report':
    split_command = command.split()
    f_command = split_command[0]
    s_command = split_command[1]

    if f_command == 'Blacklist':
        if s_command in my_list:
            index = 0
            for name in my_list:
                if name == s_command:
                    blacklisted_names += 1
                    my_list[index] = 'Blacklisted'
                    print(f"{s_command} was blacklisted.")
                index += 1
        else:
            print(f"{s_command} was not found.")

    elif f_command == 'Error':
        s_command = int(s_command)
        if s_command <= len(my_list) - 1 and s_command >= 0:
            if my_list[s_command] in my_list and my_list[s_command] != 'Blacklisted' and my_list[s_command] != 'Lost':
                lost_names += 1
                print(f"{my_list[s_command]} was lost due to an error.")
                my_list[s_command] = 'Lost'

    elif f_command == 'Change':
        s_command = int(s_command)
        new_name = split_command[2]
        if s_command <= len(my_list) - 1 and s_command >= 0:
            print(f"{my_list[s_command]} changed his username to {new_name}.")
            my_list[s_command] = new_name

    command = input()

print(f"Blacklisted names: {blacklisted_names}")
print(f"Lost names: {lost_names}")
print(' '.join(my_list))
