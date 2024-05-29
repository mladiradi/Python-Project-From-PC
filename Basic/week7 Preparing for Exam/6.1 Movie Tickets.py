
a1 = int(input())
a2 = int(input())
n = int(input())

j = int(n / 2)

for i in range(a1, a2):
    for ii in range(1, n):
        for iii in range(1, j):
            if i % 2 == 1 and (ii + iii + i) % 2 == 1:
                print(f'{chr(i)}-{ii}{iii}{i}')
