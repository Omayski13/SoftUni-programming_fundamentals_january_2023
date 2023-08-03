num_of_lines = int(input())
dict_plants = {}
for n in range(num_of_lines):
    plant, rarity = input().split("<->")
    if plant not in dict_plants:
        dict_plants[plant] = []
        dict_plants[plant].append(rarity)
        dict_plants[plant].append(0)
    else:
        dict_plants[plant][0] = rarity

command = input()
while command != "Exhibition":
    f_command, s_command = command.split(": ")
    if f_command == "Rate":
        plant, rating = s_command.split(" - ")
        if dict_plants[plant][1] == 0:
            dict_plants[plant][1] += int(rating)
        else:
            dict_plants[plant][1] += int(rating)
            dict_plants[plant][1] /= 2


    elif f_command == "Update":
        plant, new_rarity = s_command.split(" - ")
        dict_plants[plant][0] = new_rarity

    elif f_command == "Reset":
        dict_plants[s_command][1] = 0

    command = input()

print("Plants for the exhibition:")
for plant, rarity in dict_plants.items():
    print(f"- {plant}; Rarity: {rarity[0]}; Rating: {rarity[1]:.2f}")