
actor_name = input()
academy_scores = float(input())
num_jury = int(input())

total = 0

for i in range(num_jury):
    assessor_name = input()
    name_scores = 0
    for ii in assessor_name:
        name_scores += 1
    assessor_scores = float(input())
    academy_scores += (name_scores * assessor_scores) / 2
    if academy_scores > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_scores:.1f}!")
        break

if academy_scores <= 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5 - academy_scores:.1f} more!")
