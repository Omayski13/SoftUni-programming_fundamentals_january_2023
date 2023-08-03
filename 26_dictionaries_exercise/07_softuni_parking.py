num_of_commands = int(input())
registered_users ={}
for i in range(num_of_commands):
    input_command = input().split()
    command = input_command[0]
    name = input_command[1]
    if command == "register":
        license_plate = input_command[2]
        if name in registered_users:
            print(f"ERROR: already registered with plate number {registered_users[name]}")
        else:
            print(f"{name} registered {license_plate} successfully")
            registered_users[name] = license_plate
    elif command == "unregister":
        if name not in registered_users:
            print(f"ERROR: user {name} not found")
        else:
            registered_users.pop(name)
            print(f"{name} unregistered successfully")

for name,license_plate in registered_users.items():
    print(f"{name} => {license_plate}")

