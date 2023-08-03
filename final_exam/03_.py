dict_heroes = {}
command = input()
while command != "End":
    splitted_command = command.split()
    f_command = splitted_command[0]
    if f_command == "Enroll":
        hero = splitted_command[1]
        if hero not in dict_heroes:
            dict_heroes[hero] = []
        else:
            print(f"{hero} is already enrolled.")

    elif f_command == "Learn":
        hero = splitted_command[1]
        spell = splitted_command[2]
        if hero not in dict_heroes:
            print(f"{hero} doesn't exist.")
            command = input()
            continue
        else:
            if spell in dict_heroes[hero]:
                print(f"{hero} has already learnt {spell}.")
            else:
                dict_heroes[hero].append(spell)

    elif f_command == "Unlearn":
        hero = splitted_command[1]
        spell = splitted_command[2]
        if hero not in dict_heroes:
            print(f"{hero} doesn't exist.")
            command = input()
            continue
        else:
            if spell not in dict_heroes[hero]:
                print(f"{hero} doesn't know {spell}.")
            else:
                dict_heroes[hero].remove(spell)

    command = input()

# o	"Heroes:
# == {name1}: {spell1}, {spell2}, {spelln}
# == {name2}: {spell1}, {spell2}, {spelln}
# …
# == {nameN}: {spell1}, {spell2}, {spelln}"
print("Heroes:")
for hero,spells in dict_heroes.items():
    print(f'== {hero}: {", ".join(spells)}')
