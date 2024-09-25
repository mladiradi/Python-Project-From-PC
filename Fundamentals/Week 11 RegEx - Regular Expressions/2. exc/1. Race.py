
import re

participants = input().split(", ")
race_info = {}

name_pattern = re.compile(r"[A-Za-z]")
distance_pattern = re.compile(r"[0-9]")

while True:
    data = input()
    if data == "end of race":
        break

    name = "".join(name_pattern.findall(data))
    distance = sum(int(digit) for digit in distance_pattern.findall(data))

    if name in participants:
        if name in race_info:
            race_info[name] += distance
        else:
            race_info[name] = distance

sorted_racers = sorted(race_info.items(), key=lambda x: x[1], reverse=True)[:3]

places = ["1st", "2nd", "3rd"]
for i, (racer, distance) in enumerate(sorted_racers):
    print(f"{places[i]} place: {racer}")
