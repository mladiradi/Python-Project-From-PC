n = int(input())
e_sum = 0
o_sum = 0

for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 0:
        e_sum += num
    else:
        o_sum += num

if e_sum == o_sum:
    print('Yes')
    print(f'Sum = {o_sum}')
else:
    diff = abs(o_sum - e_sum)
    print('No')
    print(f'Diff = {diff}')
