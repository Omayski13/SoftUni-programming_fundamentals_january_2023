num_of_pieces = int(input())
dict_pieces = {}
for n in range(num_of_pieces):
    piece,composer, key = input().split("|")
    dict_pieces[piece] = []
    dict_pieces[piece].append(composer)
    dict_pieces[piece].append(key)

command = input()
while command != "Stop":
    splitted_command = command.split("|")
    f_command = splitted_command[0]
    if f_command == "Add":
        piece = splitted_command[1]
        composer = splitted_command[2]
        key = splitted_command[3]
        if piece not in dict_pieces:
            dict_pieces[piece] = []
            dict_pieces[piece].append(composer)
            dict_pieces[piece].append(key)
            print(f"{piece} by {composer} in {key} added to the collection!")
        elif piece in dict_pieces:
            print(f"{piece} is already in the collection!")

    elif f_command == "Remove":
        piece = splitted_command[1]
        if piece in dict_pieces:
            dict_pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif f_command == "ChangeKey":
        piece = splitted_command[1]
        new_key = splitted_command[2]
        if piece in dict_pieces:
            dict_pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        elif piece not in dict_pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for piece,keys in dict_pieces.items():
    print(f"{piece} -> Composer: {keys[0]}, Key: {keys[1]}")
