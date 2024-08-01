
students = []
course_command = ''

while True:
    command = input()
    if ":" not in command:
        course_command = command
        break

    name, id_student, course = command.split(":")
    students.append({'name': name, 'ID': id_student, 'course': course})

for student in students:
    if course_command.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['ID']}")

# # input:
#
# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals

# # result
#
# John - 5622
# Maya - 89
# Lilly - 633

# students_dict = {}
# command = input()
# while ":" in command:
#      info = command.split(":")
#      name, id, course = info[0], info[1], info[2]
#      if course not in students_dict:
#         students_dict[course] = {}
#      students_dict[course][id] = name
#      command = input()
# course = " ".join(command.split("_"))
# for key, value in students_dict.items():
#     if key == course:
#         for id, name in value.items():
#             print(f'{name} - {id}')
