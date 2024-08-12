
n = int(input())
data_base = {}

for i in range(n):
    command = input().split()

    if command[0] == "register":
        name, number = command[1], command[2]
        if name in data_base.keys():
            print(f"ERROR: already registered with plate number {number}")
        else:
            data_base[name] = number
            print(f"{name} registered {number} successfully")
    elif command[0] == "unregister":
        name = command[1]
        if name not in data_base.keys():
            print(f"ERROR: user {name} not found")
        else:
            del data_base[name]
            print(f"{name} unregistered successfully")

for name, number in data_base.items():
    print(f"{name} => {number}")

# # input:
#
# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy

# # result:
#
# John registered CS1234JS successfully
# George registered JAVA123S successfully
# Andy registered AB4142CD successfully
# Jesica registered VR1223EE successfully
# Andy unregistered successfully
# John => CS1234JS
# George => JAVA123S
# Jesica => VR1223EE
