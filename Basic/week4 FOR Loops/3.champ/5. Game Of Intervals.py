moves_in_the_game = int(input())

sc1 = 0
sc2 = 0
sc3 = 0
sc4 = 0
sc5 = 0
sc6 = 0
sum_score = 0

for i in range(0, moves_in_the_game):
    scores = int(input())

    if 0 <= scores <= 9:
        sc1 += 1
        sum_score += scores * 0.2
    elif 10 <= scores <= 19:
        sc2 += 1
        sum_score += scores * 0.3
    elif 20 <= scores <= 29:
        sc3 += 1
        sum_score += scores * 0.4
    elif 30 <= scores <= 39:
        sc4 += 1
        sum_score += 50
    elif 40 <= scores <= 50:
        sc5 += 1
        sum_score += 100
    else:
        sc6 += 1
        sum_score /= 2

print(f'{sum_score:.2f}')
print(f'From 0 to 9: {sc1 / moves_in_the_game * 100:.2f}%')
print(f'From 10 to 19: {sc2 / moves_in_the_game * 100:.2f}%')
print(f'From 20 to 29: {sc3 / moves_in_the_game * 100:.2f}%')
print(f'From 30 to 39: {sc4 / moves_in_the_game * 100:.2f}%')
print(f'From 40 to 50: {sc5 / moves_in_the_game * 100:.2f}%')
print(f'Invalid numbers: {sc6 / moves_in_the_game * 100:.2f}%')
