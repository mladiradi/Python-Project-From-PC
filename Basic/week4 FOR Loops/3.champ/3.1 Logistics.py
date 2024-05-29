cargo_num = int(input())

c1 = 0
c2 = 0
c3 = 0

for _ in range(0, cargo_num):
    load_cargo = int(input())
    if load_cargo <= 3:
        c1 += load_cargo
    elif load_cargo <= 11:
        c2 += load_cargo
    else:
        c3 += load_cargo

sum_loaded_cargo = c1 + c2 + c3
average_price_per_ton = (c1 * 200 + c2 * 175 + c3 * 120) / sum_loaded_cargo

print(f'{average_price_per_ton:.2f}')
print(f'{c1 / sum_loaded_cargo * 100:.2f}%')
print(f'{c2 / sum_loaded_cargo * 100:.2f}%')
print(f'{c3 / sum_loaded_cargo * 100:.2f}%')
