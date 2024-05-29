import sys

n = int(input())

max_n = -sys.maxsize
sum_n = 0

for _ in range(0, n):
    ent = int(input())
    if ent > max_n:
        max_n = ent
    sum_n += ent

sum_n -= max_n

if max_n == sum_n:
    print('Yes')
    print(f'Sum = {max_n}')
else:
    print('No')
    print(f'Diff = {abs(sum_n - max_n)}')
