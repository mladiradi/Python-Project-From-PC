
num_balls = int(input())
max_ball = 0
max_weight = 0
max_time = 0
max_quality = 0

for i in range(num_balls):
    weight = int(input())
    time = int(input())
    quality = int(input())

    snowball = (int(weight / time) ** quality)

    if snowball > max_ball:
        max_ball = snowball
        max_weight = weight
        max_time = time
        max_quality = quality

print(f"{max_weight} : {max_time} = {max_ball} ({max_quality})")
