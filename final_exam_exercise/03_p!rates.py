command = input()
dict_cities = {}
while command != "Sail":
    splitted_command = command.split("||")
    city = splitted_command[0]
    population = int(splitted_command[1])
    gold = int(splitted_command[2])
    if city not in dict_cities:
        dict_cities[city] = []
        dict_cities[city].append(population)
        dict_cities[city].append(gold)
    else:
        dict_cities[city][0] += population
        dict_cities[city][1] += gold

    command = input()

while command != "End":
    if command == "Sail":
        command = input()
        continue
    splitted_command = command.split("=>")
    first_commnad = splitted_command[0]
    city = splitted_command[1]
    if first_commnad == "Plunder":
        killed_people = int(splitted_command[2])
        gold = int(splitted_command[3])
        dict_cities[city][0] -= killed_people
        dict_cities[city][1] -= gold
        print(f"{city} plundered! {gold} gold stolen, {killed_people} citizens killed.")
        if dict_cities[city][0] == 0 or dict_cities[city][1] == 0:
            print(f"{city} has been wiped off the map!")
            dict_cities.pop(city)


    elif first_commnad == "Prosper":
        gold = int(splitted_command[2])
        if gold > 0:
            dict_cities[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {dict_cities[city][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")

    command = input()

if dict_cities:
    print(f"Ahoy, Captain! There are {len(dict_cities)} wealthy settlements to go to:")
    for city,values in dict_cities.items():
        print(f"{city} -> Population: {values[0]} citizens, Gold: {values[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
