
low_score = int(input())

sum_score = 0
counter = 0
low_score_counter = 0
last_prob_name = ''

while True:
    name_prob = input()
    if name_prob == 'Enough':
        print(f'Average score: {sum_score / counter:.2f}')
        print(f'Number of problems: {counter}')
        print(f'Last problem: {last_prob_name}')
        break

    score = int(input())
    if score <= 4:
        low_score_counter += 1
        if low_score_counter == low_score:
            print(f'You need a break, {low_score} poor grades.')
            break

    counter += 1
    sum_score += score
    last_prob_name = name_prob
    