import math

name = input()
episode_t = int(input())
break_t = int(input())

lunch_t = float(break_t / 8)
chill_t = float(break_t / 4)
free_t = break_t - (lunch_t + chill_t)
left_t = math.ceil(abs(free_t - episode_t))
if free_t >= episode_t:
    print(f'You have enough time to watch {name} and left with {left_t} minutes free time.')
else:
    print(f"You don't have enough time to watch {name}, you need {left_t} more minutes.")
