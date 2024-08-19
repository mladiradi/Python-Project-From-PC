
data_base = {}

while True:
    command = input()
    if command == "End":
        break

    name, employee_id = command.split(" -> ")
    if name not in data_base:
        data_base[name] = []
    if employee_id in data_base[name]:
        continue
    else:
        data_base[name].append(employee_id)

for name in data_base:
    print(name)
    for employee_id in data_base[name]:
        print(f"--{employee_id}")

# # input:
#
# SoftUni -> AA12345
# SoftUni -> CC12344
# Lenovo -> XX23456
# SoftUni -> AA12345
# Movement -> DD11111
# End

# # result:
#
# SoftUni
# -- AA12345
# -- CC12344
# Lenovo
# -- XX23456
# Movement
# -- DD11111
