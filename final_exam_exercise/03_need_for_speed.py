num_of_cars = int(input())
dict_cars = {}
for n in range(num_of_cars):
    input_car, mileage, fuel = input().split("|")
    dict_cars[input_car] = []
    dict_cars[input_car].append(int(mileage))
    dict_cars[input_car].append(int(fuel))

command = input()
while command != "Stop":
    splitted_command = command.split(" : ")
    f_command, car = splitted_command[0],splitted_command[1]
    if f_command == "Drive":
        distance = int(splitted_command[2])
        fuel = int(splitted_command[3])
        if dict_cars[car][1] >= fuel:
            dict_cars[car][1] -= fuel
            dict_cars[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
            command = input()
            continue
        if dict_cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            dict_cars.pop(car)

    elif f_command == "Refuel":
        fuel = int(splitted_command[2])
        start_fuel = dict_cars[car][1]
        dict_cars[car][1] += fuel
        if dict_cars[car][1] > 75:
            dict_cars[car][1] = 75
            loaded_fuel = 75 - start_fuel
            print(f"{car} refueled with {loaded_fuel} liters")
        else:
            print((f"{car} refueled with {fuel} liters"))

    elif f_command == "Revert":
        kilometers = int(splitted_command[2])
        start_kilometers = dict_cars[car][0]
        dict_cars[car][0] -= kilometers
        if dict_cars[car][0] < 10000:
            dict_cars[car][0] = 10000
            decreased_kilometers = start_kilometers - (start_kilometers - kilometers)
            print(f"{car} mileage decreased by {decreased_kilometers} kilometers")
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for car,values in dict_cars.items():
    print(f"{car} -> Mileage: {values[0]} kms, Fuel in the tank: {values[1]} lt.")