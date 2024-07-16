
# https://pastebin.com/Tg9hQkM7

names_lst = input().split(", ")
black_counter = 0
losted_names = 0
while True:
    command = input().split()
    if command[0] == "Report":
        break
    elif command[0] == "Blacklist":
        name = command[1]
        for i in range(len(names_lst)):
            if names_lst[i] == name:
                print(f"{name} was blacklisted.")
                names_lst[i] = "Blacklisted"
                black_counter += 1
        if black_counter == 0:
            print(f"{name} was not found.")

    elif command[0] == "Error":
        index = command[1]
        if int(index) in range(len(names_lst)):
            if names_lst[int(index)] != "Blacklisted" and names_lst[int(index)] != "Lost":
                print(f"{names_lst[int(index)]} was lost due to an error.")
                names_lst[int(index)] = "Lost"
                losted_names += 1

    elif command[0] == "Change":
        index = command[1]
        new_name = command[2]
        if int(index) in range(len(names_lst)):
            name = names_lst[int(index)]
            names_lst[int(index)] = new_name
            print(f"{name} changed his username to {new_name}.")

print(f"Blacklisted names: {black_counter}")
print(f"Lost names: {losted_names}")
print(' '.join(names_lst))
