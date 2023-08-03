command = input()
courses = {}
while command != "end":
    course_name, student_name = command.split(" : ")

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input()

for course_name,students in courses.items():
    print(f"{course_name}: {len(courses[course_name])}")

    for student_name in students:
        print(f"-- {student_name}")







