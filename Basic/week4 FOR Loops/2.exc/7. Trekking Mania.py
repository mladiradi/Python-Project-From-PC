group_num = int(input())

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

for i in range(0, group_num):
    hikers_num = int(input())
    if hikers_num <= 5:
        g1 += hikers_num
    elif hikers_num <= 12:
        g2 += hikers_num
    elif hikers_num <= 25:
        g3 += hikers_num
    elif hikers_num <= 40:
        g4 += hikers_num
    else:
        g5 += hikers_num

total_hikers = g1 + g2 + g3 + g4 + g5

print(f'{g1 / total_hikers * 100:.2f}%')
print(f'{g2 / total_hikers * 100:.2f}%')
print(f'{g3 / total_hikers * 100:.2f}%')
print(f'{g4 / total_hikers * 100:.2f}%')
print(f'{g5 / total_hikers * 100:.2f}%')
