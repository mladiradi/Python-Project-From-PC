name_actor = input()
score_academy = float(input())
count_juri = int(input())

for i in range(0, count_juri):
    name_juri = input()
    score_juri = float(input())
    count = 0
    for _ in range(0, len(name_juri)):
        count += 1
    score_academy += (count * score_juri) / 2
    if score_academy >= 1250.5:
        print(f'Congratulations, {name_actor} got a nominee for leading role with {score_academy:.1f}!')
        exit()

left_scores = abs(score_academy - 1250.5)
print(f'Sorry, {name_actor} you need {left_scores:.1f} more!')
