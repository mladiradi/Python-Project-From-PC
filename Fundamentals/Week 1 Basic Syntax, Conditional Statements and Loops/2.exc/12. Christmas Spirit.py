
quantity_of_decorations = int(input())
days_to_christmas = int(input())

total_money = 0
total_spirit = 0

ornament_set_pr = 2
skirt_pr = 5
garland_pr = 3
lights_pr = 15

ornament_sp = 5
skirt_sp = 3
garland_sp = 10
lights_sp = 17

for days in range(1, days_to_christmas + 1):
    if days % 11 == 0:
        quantity_of_decorations += 2
    if days % 2 == 0:
        total_money += ornament_set_pr * quantity_of_decorations
        total_spirit += ornament_sp
    if days % 3 == 0:
        total_money += (skirt_pr + garland_pr) * quantity_of_decorations
        total_spirit += skirt_sp + garland_sp
    if days % 5 == 0:
        total_money += lights_pr * quantity_of_decorations
        total_spirit += lights_sp
        if days % 3 == 0:
            total_spirit += 30
    if days % 10 == 0:
        total_spirit -= 20
        total_money += skirt_pr + garland_pr + lights_pr

if days_to_christmas % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_money}")
print(f"Total spirit: {total_spirit}")
