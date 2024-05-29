
sum_steps = 0

while True:
    text = input()

    if text == 'Going home':
        steps = int(input())
        sum_steps += steps
        if sum_steps < 10000:
            print(f'{abs(10000 - sum_steps)} more steps to reach goal.')
            break
    else:
        steps = int(text)
        sum_steps += steps

    if sum_steps >= 10000:
        print("Goal reached! Good job!")
        print(f'{abs(10000 - sum_steps)} steps over the goal!')
        break
