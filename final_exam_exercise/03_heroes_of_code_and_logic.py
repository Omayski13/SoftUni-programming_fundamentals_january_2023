num_of_heroes = int(input())
dict_heroes = {}
for n in range(num_of_heroes):
    hero, hp, mp = input().split()
    dict_heroes[hero] = []
    dict_heroes[hero].append(int(hp))
    if dict_heroes[hero][0] > 100:
        dict_heroes[hero][0] = 100
    dict_heroes[hero].append(int(mp))
    if dict_heroes[hero][1] > 200:
        dict_heroes[hero][1] = 200

command = input()
while command != "End":
    splitted_command = command.split(" - ")
    f_command = splitted_command[0]

    if f_command == "CastSpell":
        hero = splitted_command[1]
        mp_needed = int(splitted_command[2])
        spell_name = splitted_command[3]
        if dict_heroes[hero][1] >= mp_needed:
            dict_heroes[hero][1] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {dict_heroes[hero][1]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif f_command == "TakeDamage":
        hero = splitted_command[1]
        damage = int(splitted_command[2])
        attacker = splitted_command[3]
        dict_heroes[hero][0] -= damage
        if dict_heroes[hero][0] <= 0:
            print(f"{hero} has been killed by {attacker}!")
            dict_heroes.pop(hero)
        else:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {dict_heroes[hero][0]} HP left!")

    elif f_command == "Heal":
        hero = splitted_command[1]
        amount = int(splitted_command[2])
        start_hp = dict_heroes[hero][0]
        dict_heroes[hero][0] += amount
        if dict_heroes[hero][0] > 100:
            dict_heroes[hero][0] = 100
            healed_hp = 100 - start_hp
            print(f"{hero} healed for {healed_hp} HP!")
        else:
            print(f"{hero} healed for {amount} HP!")

    elif f_command == "Recharge":
        hero = splitted_command[1]
        amount = int(splitted_command[2])
        start_mp = dict_heroes[hero][1]
        dict_heroes[hero][1] += amount
        if dict_heroes[hero][1] > 200:
            dict_heroes[hero][1] = 200
            healed_mp = 200 - start_mp
            print(f"{hero} recharged for {healed_mp} MP!")
        else:
            print(f"{hero} recharged for {amount} MP!")

    command = input()

for hero,values in dict_heroes.items():
    print(hero)
    print(f"  HP: {values[0]}")
    print(f"  MP: {values[1]}")
