
n = int(input())

sum_tok = 0

for _ in range(0, n):

    tok = float(input())
    sum_tok += tok

water = n * 20
inter = n * 15
other = (sum_tok + water + inter) * 1.2
average = (sum_tok + water + inter + other) / n

print(f'Electricity: {sum_tok:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {inter:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')
