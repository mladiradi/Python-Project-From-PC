
wins = 0
losts = 0
games = 0

while True:
    name = input()
    if name == 'End of tournaments':
        print(f'{(wins / games) * 100:.2f}% matches win')
        print(f'{(losts / games) * 100:.2f}% matches lost')
        break

    n_games = int(input())
    for i in range(1, n_games + 1):

        team_1 = int(input())
        team_2 = int(input())

        result = abs(team_1 - team_2)
        games += 1

        if team_1 > team_2:
            print(f'Game {i} of tournament {name}: win with {result} points.')
            wins += 1
        else:
            print(f'Game {i} of tournament {name}: lost with {result} points.')
            losts += 1
