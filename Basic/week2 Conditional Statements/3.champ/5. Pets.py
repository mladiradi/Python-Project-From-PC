import math

days = int(input())
food_kg = int(input())
dog_d_f = float(input())
cat_d_f = float(input())
turtle_d_f = float(input()) / 1000

needed_f = days * (dog_d_f + cat_d_f + turtle_d_f)
wanted_f = abs(food_kg - needed_f)

if needed_f < food_kg:
    print(f'{math.floor(wanted_f)} kilos of food left.')
else:
    print(f'{math.ceil(wanted_f)} more kilos of food are needed.')
