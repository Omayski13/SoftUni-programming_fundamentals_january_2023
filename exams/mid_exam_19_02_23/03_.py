def phone_in_list(phone):
    if phone in my_list:
        return True

my_list = [el for el in input().split(', ')]
command = input()

while command != 'End':
    split_command = command.split(' - ')
    f_command = split_command[0]
    phone = split_command[1]
    if f_command == 'Add':
        if not phone_in_list(phone):
            my_list.append(phone)

    elif f_command == 'Remove':
        if phone_in_list(phone):
            my_list.remove(phone)

    elif f_command == 'Bonus phone':
        split_phone = phone.split(':')
        old_phone = split_phone[0]
        new_phone = split_phone[1]
        if phone_in_list(old_phone):
            index = 0
            for i in my_list:
                if i == old_phone:
                    my_list.insert(index + 1, new_phone)
                index += 1
    elif f_command == 'Last':
        if phone_in_list(phone):
            my_list.remove(phone)
            my_list.append(phone)
    command = input()


print(', '.join(my_list))