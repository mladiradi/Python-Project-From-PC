import math

tour_part = int(input())
start_points = int(input())

scores = 0
counter = 0

for _ in range(0, tour_part):
    stage = input()

    if stage == 'W':
        scores += 2000
        counter += 1
    elif stage == 'F':
        scores += 1200
    elif stage == 'SF':
        scores += 720

total_scores = scores + start_points

print(f'Final points: {total_scores}')
print(f'Average points: {math.floor(scores / tour_part)}')
print(f'{counter / tour_part * 100:.2f}%')
