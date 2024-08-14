
course_d = {}

while True:
    line = input()
    if line == "end":
        break

    course, student = line.split(" : ")

    if course not in course_d:
        course_d[course] = []

    course_d[course].append(student)

for course, students in course_d.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")

# # input:
#
# Programming Fundamentals : John Smith
# Programming Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java Advanced : Harrison White
# end

# # result:
#
# Programming Fundamentals: 2
# -- John Smith
# -- Linda Johnson
# JS Core: 1
# -- Will Wilson
# Java Advanced: 1
# -- Harrison White
