input_command = input()
dict ={}

while ":" in input_command:
    name, name_id, course = input_command.split(":")
    if course not in dict:
        dict[course] = {name_id : name}
    else:
        dict[course][name_id] = name

    input_command = input()
course_name = input_command.replace("_"," ")

for name_id, name in dict[course_name].items():
    print(f"{name} - {name_id}")
