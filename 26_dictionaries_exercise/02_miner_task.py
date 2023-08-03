command = input()
dict = {}
while command != "stop":
    resource = command
    quantity = int(input())
    if resource not in dict:
        dict[resource] = quantity
    else:
        dict[resource] += quantity
    command = input()

# for resource,quantity in dict.items():
#     print(f"{resource} -> {quantity}")

result = [f'{resource} -> {quantity}' for resource, quantity in dict.items()]
print("\n".join(result))