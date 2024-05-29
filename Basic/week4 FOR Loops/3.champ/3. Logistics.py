cargo_num = int(input())

bus_price_per_ton = 0
bus_load_cargo = 0
truck_price_per_ton = 0
truck_load_cargo = 0
train_price_per_ton = 0
train_load_cargo = 0
sum_loaded_cargo = 0

for _ in range(0, cargo_num):
    load_cargo = int(input())
    sum_loaded_cargo += load_cargo
    if load_cargo <= 3:
        bus_price_per_ton += load_cargo * 200
        bus_load_cargo += load_cargo
    elif load_cargo <= 11:
        truck_price_per_ton += load_cargo * 175
        truck_load_cargo += load_cargo
    else:
        train_price_per_ton += load_cargo * 120
        train_load_cargo += load_cargo

total_price = bus_price_per_ton + truck_price_per_ton + train_price_per_ton
average_price_per_ton = total_price / sum_loaded_cargo

print(f'{average_price_per_ton:.2f}')
print(f'{bus_load_cargo / sum_loaded_cargo * 100:.2f}%')
print(f'{truck_load_cargo / sum_loaded_cargo * 100:.2f}%')
print(f'{train_load_cargo / sum_loaded_cargo * 100:.2f}%')
