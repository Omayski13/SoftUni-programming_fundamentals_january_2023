command = input()
dict = {}
while "-" in command:
    name, number = command.split("-")
    dict[name] = number
    command = input()

command = int(command)

for names in range(command):
    name = input()
    if name in dict:
        print(f"{name} -> {dict[name]}")
    else:
        print(f"Contact {name} does not exist.")

