import math

magn_n = int(input()) * 3.25
zumb_n = int(input()) * 4
rose_n = int(input()) * 3.5
cact_n = int(input()) * 8
gift_p = float(input())

profit = (magn_n + zumb_n + rose_n + cact_n) * (1 - 0.05)
wanted = abs(profit - gift_p)

if profit >= gift_p:
    print(f'She is left with {math.floor(wanted)} leva.')
else:
    print(f'She will have to borrow {math.ceil(wanted)} leva.')
