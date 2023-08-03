command = input()
dict = {}
while command != 'End':
    company_name,employee_id = command.split(" -> ")
    if company_name not in dict:
        dict[company_name] = []
    if employee_id not in dict[company_name]:
        dict[company_name].append(employee_id)

    command = input()

for company_name,employee_id in dict.items():
    print(company_name)
    for employee in employee_id:
        print(f"-- {employee}")

