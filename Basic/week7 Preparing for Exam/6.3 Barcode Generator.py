
start = input()
stop = input()

a1 = 0
a2 = 0
a3 = 0
a4 = 0
b1 = 0
b2 = 0
b3 = 0
b4 = 0
count = 0

for a in start:
    if count == 0:
        a1 = int(a)
    elif count == 1:
        a2 = int(a)
    elif count == 2:
        a3 = int(a)
    else:
        a4 = int(a)
    count += 1
count = 0

for b in stop:
    if count == 0:
        b1 = int(b)
    elif count == 1:
        b2 = int(b)
    elif count == 2:
        b3 = int(b)
    else:
        b4 = int(b)
    count += 1
count = 0

for i in range(a1, b1 + 1):
    for ii in range(a2, b2 + 1):
        for iii in range(a3, b3 + 1):
            for iiii in range(a4, b4 + 1):
                if i % 2 != 0 and ii % 2 != 0 and iii % 2 != 0 and iiii % 2 != 0:
                    print(f'{i}{ii}{iii}{iiii}', end=' ')

# start_number = input()
# end_number = input()
# n_1 = 0
# n_2 = 0
# n_3 = 0
# n_4 = 0
# e_1 = 0
# e_2 = 0
# e_3 = 0
# e_4 = 0
# for x, number in enumerate(start_number):
#     if x == 0:
#         n_1 = int(number)
#     elif x == 1:
#         n_2 = int(number)
#     elif x == 2:
#         n_3 = int(number)
#     else:
#         n_4 = int(number)
# for y, number_end in enumerate(end_number):
#     if y == 0:
#         e_1 = int(number_end)
#     elif y == 1:
#         e_2 = int(number_end)
#     elif y == 2:
#         e_3 = int(number_end)
#     else:
#         e_4 = int(number_end)
# for a in range(n_1, e_1 + 1):
#     for b in range(n_2, e_2 + 1):
#         for c in range(n_3, e_3 + 1):
#             for d in range(n_4, e_4 + 1):
#                 if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
#                     print(f'{a}{b}{c}{d}', end=' ')
