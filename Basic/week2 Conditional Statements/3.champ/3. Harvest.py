import math

X = int(input())
Y = float(input())
Z = int(input())
N = int(input())


grape_kg = (X * Y) * (1 - 0.6)
wine_lt = grape_kg / 2.5
bonus = abs(wine_lt - Z)
worker_b = bonus / N

if wine_lt >= Z:
    print(f"Good harvest this year! Total wine: {math.floor(wine_lt)} liters.")
    print(f"{math.ceil(bonus)} liters left -> {math.ceil(worker_b)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(bonus)} liters wine needed.")
