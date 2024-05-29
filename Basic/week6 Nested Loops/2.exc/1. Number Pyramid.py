
num = int(input())

current = 1

for row in range(1, num + 1):
    for col in range(1, row + 1):
        if current > num:
            break
        print(str(current) + ' ', end='')
        current += 1
    if current > num:
        break
    print()


# n = int(input())
#
# current = 1
# current_bigger_than_n = False
#
# for row in range(1, n + 1):
#     for col in range(1, row + 1):
#         if current > n:
#             current_bigger_than_n = True
#             break
#         print(str(current) + ' ', end='')
#         current += 1
#     if current_bigger_than_n:
#         break
#     print()


# number = int(input())
# n = 1
#
# for i in range(1, number + 1):
#     for ii in range(i):
#         if number >= n:
#             print(n, end=" ")
#             n += 1
#     print()
#