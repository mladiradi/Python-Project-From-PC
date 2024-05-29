import sys
max_n = -sys.maxsize
min_n = sys.maxsize

n = int(input())

for i in range(0, n):
    num = int(input())
    if num > max_n:
        max_n = num
    if num < min_n:
        min_n = num

print(f'Max number: {max_n}')
print(f'Min number: {min_n}')
