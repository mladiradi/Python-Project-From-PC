juniors = int(input())
seniors = int(input())
trace = input()

tax_j = 0
tax_s = 0

if trace == 'trail':
    tax_j = juniors * 5.5
    tax_s = seniors * 7
elif trace == 'cross-country':
    tax_j = juniors * 8
    tax_s = seniors * 9.5
elif trace == 'downhill':
    tax_j = juniors * 12.25
    tax_s = seniors * 13.75
elif trace == 'road':
    tax_j = juniors * 20
    tax_s = seniors * 21.5

tax_sum = tax_s + tax_j

if trace == 'cross-country' and (juniors + seniors) >= 50:
    tax_sum = (tax_sum * 0.75) * 0.95
else:
    tax_sum *= 0.95

print(f'{tax_sum:.2f}')
