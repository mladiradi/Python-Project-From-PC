
train_wagons = int(input())
train_wagons_lst = [0] * train_wagons

while True:
    command = input().split()

    if command[0] == "End":
        print(train_wagons_lst)
        break
    elif command[0] == "add":
        people_num = int(command[1])
        train_wagons_lst[-1] += people_num
    elif command[0] == "insert":
        people_num = int(command[2])
        train_wagons_lst[int(command[1])] += people_num
    elif command[0] == "leave":
        wagon = int(command[1])
        people_num = int(command[2])
        train_wagons_lst[wagon] -= people_num
