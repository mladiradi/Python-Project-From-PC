
counter = 0
eggs = 0

budget = float(input())
price_for_kg_flour = float(input())

price_for_pack_of_eggs = price_for_kg_flour * 0.75
price_for_L_milk = (price_for_kg_flour * 1.25) / 4
price_of_1_bread = price_for_kg_flour + \
                   price_for_pack_of_eggs + \
                   price_for_L_milk

while budget >= price_of_1_bread:

    budget -= price_of_1_bread
    eggs += 3
    counter += 1

    if counter % 3 == 0:
        eggs -= counter - 2

print(f"You made {counter} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")
