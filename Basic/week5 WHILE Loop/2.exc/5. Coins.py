
change = float(input())
cents = int(change * 100)
counter = 0

while True:
    counter += 1
    if cents >= 200:
        cents -= 200
    elif cents >= 100:
        cents -= 100
    elif cents >= 50:
        cents -= 50
    elif cents >= 20:
        cents -= 20
    elif cents >= 10:
        cents -= 10
    elif cents >= 5:
        cents -= 5
    elif cents >= 2:
        cents -= 2
    else:
        cents -= cents

    if cents == 0:
        print(counter)
        break
