
expected_sum = int(input())

counter = 0
cash_counter = 0
card_counter = 0
sum_money = 0
sum_cash = 0
sum_card = 0

while True:
    text = input()
    if text == 'End':
        print("Failed to collect required money for charity.")
        break

    money = int(text)

    if counter % 2 == 0:
        if money > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            sum_money += money
            sum_cash += money
            cash_counter += 1
    else:
        if money < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            sum_money += money
            sum_card += money
            card_counter += 1

    counter += 1

    if sum_money >= expected_sum:
        print(f"Average CS: {sum_cash / cash_counter:.2f}")
        print(f"Average CC: {sum_card / card_counter:.2f}")
        break
