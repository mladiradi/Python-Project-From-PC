
lst_of_gifts = input().split()

value = "None"

while True:
    command = input()
    if command != "No Money":
        lst_of_command = command.split()
    else:
        break
    if "OutOfStock" in lst_of_command:  # replacing value with "None"
        for i in range(len(lst_of_gifts)):
            if lst_of_gifts[i] == lst_of_command[1]:
                lst_of_gifts[i] = value
    elif "Required" in lst_of_command:  # replacing index value with lst_command[1]
        if 0 <= int(lst_of_command[2]) <= len(lst_of_gifts):
            index = int(lst_of_command[2])
            for i in range(len(lst_of_gifts)):
                if i == index:
                    lst_of_gifts[index] = lst_of_command[1]
    elif "JustInCase" in lst_of_command:  # replacing last value with lst_command[1]
        for i in range(len(lst_of_gifts)):
            if i == (len(lst_of_gifts) - 1):
                lst_of_gifts.remove(lst_of_gifts[i])
        lst_of_gifts.append(lst_of_command[1])
    lst_of_command = []

for i in range(len(lst_of_gifts)):  # removing "None" values
    if value in lst_of_gifts:
        lst_of_gifts.remove(value)

for i in range(len(lst_of_gifts) - 1):  # printing without last space
    print(lst_of_gifts[i], end=" ")
print(lst_of_gifts[-1])
