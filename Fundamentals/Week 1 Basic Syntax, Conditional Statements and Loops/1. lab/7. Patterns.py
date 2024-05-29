
# num = int(input())
#
# for i in range(1, num + 1):
#     for j in range(0, i):
#         print('*', end='')
#     print()
# for ii in range(num-1, 0, -1):
#     for j in range(0, ii):
#         print('*', end='')
#     print()


# num = int(input())
#
# for i in range(0, num):
#     if not 1 <= i <= (num - 2):
#         for j in range(0, num):
#             print('*', end='')
#             continue
#         print()
#     else:
#         for ii in range(0, num):
#             if 1 <= ii <= (num - 2):
#                 print(end=' ')
#                 continue
#             print('*', end='')
#         print()

n = int(input())

for i in range(1, n + 1): # Loop through rows

    for j in range(1, n + 1): # Loop to print pattern

        if (i == 1 or i == n or j == 1 or j == n): # Printing Pattern
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()
