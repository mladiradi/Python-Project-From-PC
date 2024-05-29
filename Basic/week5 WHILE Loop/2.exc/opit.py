need_money = float(input())
cash_money = float(input())

counter = 1
spend_counter = 0

while True:

    action = input()
    action_money = float(input())

    if action == 'spend':
        cash_money -= action_money
        spend_counter += 1

        if cash_money < 0:
            cash_money = 0

    if action == 'save':
        cash_money += action_money
        spend_counter = 0

    if spend_counter >= 5:
        print("You can't save the money.")
        print(counter)
        break

    if cash_money >= need_money:
        print(f'You saved the money for {counter} days.')
        break

    counter += 1
