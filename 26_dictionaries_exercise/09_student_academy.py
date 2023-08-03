num_of_pairs = int(input())
dict = {}
for i in range(num_of_pairs):
    name = input()
    grade = float(input())
    if name not in dict:
        dict[name] = []
    dict[name].append(float(grade))

for name,grade in dict.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
