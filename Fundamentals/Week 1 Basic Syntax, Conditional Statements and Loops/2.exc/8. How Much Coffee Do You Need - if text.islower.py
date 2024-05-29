
text = input()

coffee = 0

while text != 'END':

    if text.lower() == 'coding' or text.lower() == 'dog' or \
            text.lower() == 'cat' or text.lower() == 'movie':

        if text.islower():
            coffee += 1
        else:
            coffee += 2

    text = input()

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
