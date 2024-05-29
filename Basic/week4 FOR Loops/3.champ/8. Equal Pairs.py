import sys
n = int(input())

dif = 0
prev_p = 0
max_dif = -sys.maxsize
i = 1

for _ in range(0, n):
    for _ in range(1, i + 1):
        p1 = int(input())
        p2 = int(input())
        sumes_p = p1 + p2

        dif = sumes_p - prev_p
        prev_p = sumes_p

        if dif > max_dif:
            max_dif = dif

        sum_p = 0

if n == 1:
    print(f'Yes, value={dif}')
elif dif != 0:
    print(f'No, maxdiff={abs(dif)}')
else:
    print(f'Yes, value={prev_p}')
