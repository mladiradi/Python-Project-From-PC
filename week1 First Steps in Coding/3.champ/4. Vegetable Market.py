veggie_p = float(input())
fruit_p = float(input())
veggie_kg = int(input())
fruit_kg = int(input())

total = ((veggie_kg * veggie_p) + (fruit_kg * fruit_p)) / 1.94

print('%.2f' % total)
