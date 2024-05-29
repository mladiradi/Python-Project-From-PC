
straw_p = float(input())
banana_kg = float(input())
porto_kg = float(input())
malin_kg = float(input())
straw_kg = float(input())

malin_p = straw_p / 2
malin_money = malin_kg * malin_p
porto_money = porto_kg * (malin_p * 0.6)
banana_money = banana_kg * (malin_p * 0.2)
straw_money = straw_kg * straw_p

need_money = malin_money + porto_money + banana_money + straw_money

print(f'{need_money:.2f}')
