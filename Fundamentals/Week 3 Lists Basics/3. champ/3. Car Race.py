
numbers = list(map(int, input().split()))

left_car = 0
right_car = 0

middle_index = len(numbers) // 2 + 1

for i in numbers[0:middle_index - 1]:
    left_car += int(i)

    if int(i) == 0:
        left_car *= 0.80

for j in numbers[len(numbers):middle_index - 1:-1]:
    right_car += int(j)

    if int(j) == 0:
        right_car *= 0.80

if left_car > right_car:
    print(f"The winner is right with total time: {right_car:.1f}")
else:
    print(f"The winner is left with total time: {left_car:.1f}")
