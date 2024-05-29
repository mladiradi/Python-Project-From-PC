
stad_cap = int(input())
fans_num = int(input())

f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0

for i in range(0, fans_num):
    sector = input()
    if sector == 'A':
        f1 += 1
    elif sector == 'B':
        f2 += 1
    elif sector == 'V':
        f3 += 1
    elif sector == 'G':
        f4 += 1

print(f'{f1 / fans_num * 100:.2f}%')
print(f'{f2 / fans_num * 100:.2f}%')
print(f'{f3 / fans_num * 100:.2f}%')
print(f'{f4 / fans_num * 100:.2f}%')
print(f'{fans_num / stad_cap * 100:.2f}%')
