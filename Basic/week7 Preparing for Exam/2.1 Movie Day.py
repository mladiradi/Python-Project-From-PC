import math

time_limit = int(input())
scenes_num = int(input())
time_per_scene = int(input())

prep_time = time_limit * 0.15
scenes_time = (scenes_num * time_per_scene) + prep_time
result = abs(math.ceil(time_limit - scenes_time))

if time_limit >= scenes_time:
    print(f"You managed to finish the movie on time! You have {result} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {result} minutes.")