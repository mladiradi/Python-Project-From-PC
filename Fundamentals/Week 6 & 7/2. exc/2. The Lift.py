
people = int(input())
lift_wagons = list(map(int, input().split()))

for wagon in range(len(lift_wagons)):
    if people > 3:
        diff = abs(4 - int(lift_wagons[wagon]))
        lift_wagons[wagon] += diff
        people -= diff
    else:
        lift_wagons[wagon] += people
        people = 0

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif sum(lift_wagons) != len(lift_wagons) * 4:
    print("The lift has empty spots!")

print(" ".join(map(str, lift_wagons)))

# people = int(input())
#
# lift = [int(cart) for cart in input().split(" ")]
#
# for i in range(len(lift)):
#     can_load = min(4 - lift[i], people)
#     lift[i] += can_load
#     people -= can_load
#
# if people > 0:
#     print(f"There isn't enough space! {people} people in a queue!")
# elif len([cart for cart in lift if cart < 4]) > 0:
#     print("The lift has empty spots!")
#
# print(" ".join([str(cart) for cart in lift]))
