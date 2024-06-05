
main_input = input().split("|")
start_energy = 100
start_coins = 100

closed = False
text = ""

for i in main_input:
    event_and_number = i.split("-")
    text = event_and_number[0]
    value = int(event_and_number[1])

    if text == "rest":
        init_energy = start_energy
        start_energy += value
        if start_energy > 100:  # no need to add energy over 100
            start_energy = 100
        gain_energy = start_energy - init_energy
        print(f"You gained {gain_energy} energy.")
        print(f"Current energy: {start_energy}.")

    elif text == "order":
        if start_energy >= 30:
            start_coins += value
            start_energy -= 30
            print(f"You earned {value} coins.")
        else:
            start_energy += 50
            print("You had to rest!")

    else:
        if start_coins >= value:
            start_coins -= value
            print(f"You bought {text}.")
        else:
            closed = True
            break

if closed:
    print(f"Closed! Cannot afford {text}.")
else:
    print("Day completed!")
    print(f"Coins: {start_coins}")
    print(f"Energy: {start_energy}")
