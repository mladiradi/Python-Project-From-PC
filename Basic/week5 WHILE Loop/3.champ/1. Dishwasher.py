
bottles = int(input())

detergent_ml = bottles * 750
counter = 0
counter_pots = 0
counter_dishes = 0

while True:
    text = input()

    if text == 'End':
        print(f"Detergent was enough!")
        print(f"{counter_dishes} dishes and {counter_pots} pots were washed.")
        print(f"Leftover detergent {detergent_ml} ml.")
        break

    dishes = int(text)
    counter += 1

    if counter % 3 != 0:
        detergent_ml -= dishes * 5
        counter_dishes += dishes
    else:
        detergent_ml -= dishes * 15
        counter_pots += dishes

    if detergent_ml < 0:
        print(f"Not enough detergent, {abs(detergent_ml)} ml. more necessary!")
        break
