num_of_lines = int(input())
dict_plant = {}
for n in range(num_of_lines):
    plant, rarity = input().split("<->")
    if plant not in dict_plant:
        dict_plant[plant] = []
        dict_plant[plant].append(rarity)
        dict_plant[plant].append(0)
    else:
        dict_plant[plant][0] = rarity

command = input()
while command != 'Exhibition':
    f_commnad, s_command = command.split(': ')
    if f_commnad == 'Rate':
        splitted_s_command = s_command.split(' - ')
        plant = splitted_s_command[0]
        rating = int(splitted_s_command[1])
        if plant in dict_plant:
            if dict_plant[plant][1] > 0:
                dict_plant[plant][1] = (dict_plant[plant][1] + rating) / 2
            else:
                dict_plant[plant][1] = rating
        else:
            print("error")
            command = input()
            continue

    elif f_commnad == 'Update':
        splitted_s_command = s_command.split(' - ')
        plant = splitted_s_command[0]
        new_rarity = int(splitted_s_command[1])
        if plant in dict_plant:
            dict_plant[plant][0] = new_rarity
        else:
            print("error")
            command = input()
            continue

    elif f_commnad == 'Reset':
        plant = s_command
        if plant in dict_plant:
            dict_plant[plant][1] = 0
        else:
            print("error")
            command = input()
            continue

    command = input()

print("Plants for the exhibition:")
for plant,values in dict_plant.items():
    print(f"- {plant}; Rarity: {values[0]}; Rating: {values[1]:.2f}")

