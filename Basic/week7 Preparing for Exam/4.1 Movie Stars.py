
budget = float(input())

while True:
    text = input()
    counter = 0

    if text == 'ACTION':
        print(f"We are left with {budget:.2f} leva.")
        break
    for i in text:
        counter += 1
    if counter <= 15:
        salary = float(input())
        budget -= salary
    else:
        budget *= 0.8
    if budget < 0:
        print(f"We need {(abs(budget)):.2f} leva for our actors.")
        break
