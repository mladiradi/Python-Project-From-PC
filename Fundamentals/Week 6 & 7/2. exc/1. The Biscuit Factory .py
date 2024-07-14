
import math

num_biscuits_per_worker = int(input())
count_of_workers = int(input())
competing_factory_produces_month = int(input())

daily_production = num_biscuits_per_worker * count_of_workers
month_production = 0
for i in range(1, 31):

    if i % 3 == 0:
        reduced_production = math.floor(daily_production * 0.75)
        month_production += reduced_production
    else:
        month_production += daily_production

diff = abs(month_production - competing_factory_produces_month)
percentage_production = diff / competing_factory_produces_month * 100

print(f"You have produced {month_production} biscuits for the past month.")

if month_production > competing_factory_produces_month:
    print(f"You produce {percentage_production:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage_production:.2f} percent less biscuits.")
