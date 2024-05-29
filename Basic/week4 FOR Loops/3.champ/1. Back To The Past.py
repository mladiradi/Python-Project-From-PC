money_inheritance = float(input())
year_of_death = int(input())

money_for_whores = 0
years_of_partying = 18

for _ in range(1800, year_of_death + 1):
    if years_of_partying % 2 == 0:
        money_for_whores = 12000
        years_of_partying += 1
        money_inheritance -= money_for_whores
    else:
        money_for_whores = 12000 + (years_of_partying * 50)
        years_of_partying += 1
        money_inheritance -= money_for_whores

if money_inheritance >= 0:
    print(f'Yes! He will live a carefree life and will have {money_inheritance:.2f} dollars left.')
else:
    print(f'He will need {abs(money_inheritance):.2f} dollars to survive.')
