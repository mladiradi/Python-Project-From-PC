n = int(input())
l_sum = 0
r_sum = 0

for i in range(1, n + 1):
    num = int(input())
    l_sum = l_sum + num

for i in range(1, n + 1):
    num = int(input())
    r_sum = r_sum + num

if r_sum == l_sum:
    print(f'Yes, sum = {l_sum}')
else:
    diff = abs(r_sum - l_sum)
    print(f'No, diff = {diff}')
