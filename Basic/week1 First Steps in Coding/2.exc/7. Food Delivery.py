chicken = float(int(input()) * 10.35)
fish = float(int(input()) * 12.4)
veggie = float(int(input()) * 8.15)

menu_sum = chicken + fish + veggie
total_sum = menu_sum * (1 + 0.2) + 2.5

print(total_sum)
