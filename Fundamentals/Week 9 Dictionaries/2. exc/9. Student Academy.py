
num = int(input())
students = {}
name_lst = []

for _ in range(num):
    name = input()
    score = float(input())

    if name not in students:
        students[name] = 0.0
    students[name] += score
    name_lst.append(name)

for name in students:
    average_score = students[name] / name_lst.count(name)
    if average_score >= 4.5:
        print(f"{name} -> {average_score:.2f}")

# # input:
#
# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5

# # result:
#
# John -> 5.00
# Alice -> 4.50
# George -> 5.00
