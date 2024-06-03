# team_a = ["A-" + str(number) for number in range(1, 12)]  # list comprehension
# team_b = ["B-" + str(number) for number in range(1, 12)]
# print(team_a)
# print(team_b)

team_a = []
team_b = []
lst_red_cards = []
game_over = False

for i in range(1, 12):
    string = str(i)
    team_a.append(f"A-{string}")
    team_b.append(f"B-{string}")

lst_red_cards = input().split()

for i in lst_red_cards:
    if i in team_a:
        team_a.remove(i)
    elif i in team_b:
        team_b.remove(i)

    if len(team_a) < 7 or len(team_b) < 7:
        game_over = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_over:
    print("Game was terminated")
