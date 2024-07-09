# 2
def loot(current_treasure_chest: list, items: list) -> list:
    for item in items:
        if item not in current_treasure_chest:
            current_treasure_chest.insert(0, item)
    return current_treasure_chest


def drop(current_treasure_chest, current_index):
    if current_index in range(len(current_treasure_chest)):
        current_treasure_chest.append(current_treasure_chest.pop(current_index))
    return current_treasure_chest


def steal(current_treasure_chest, current_steal_count):
    if current_steal_count >= len(current_treasure_chest):
        print(", ".join(current_treasure_chest))
        return []
    steal_index = len(current_treasure_chest) - current_steal_count
    print(", ".join(current_treasure_chest[steal_index:]))
    current_treasure_chest = current_treasure_chest[:steal_index]
    return current_treasure_chest


treasure_chest = input().split("|")
command = input().split()
while command[0] != "Yohoho!":
    action = command[0]
    if action == "Loot":
        treasure_chest = loot(treasure_chest, command[1:])
    elif action == "Drop":
        index = int(command[1])
        treasure_chest = drop(treasure_chest, index)
    elif action == "Steal":  # else
        count = int(command[1])
        treasure_chest = steal(treasure_chest, count)
    command = input().split()
if not treasure_chest:  # if treasure_chest == 0
    print("Failed treasure hunt.")
else:
    average = sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average:.2f} pirate credits.")

# 2.1

# treasure_chest = input().split("|")
# command = input().split()
# while command[0] != "Yohoho!":
#     action = command[0]
#     if action == "Loot":
#         items = command[1:]
#         for item in items:
#             if item not in treasure_chest:
#                 treasure_chest.insert(0, item)
#     elif action == "Drop":
#         index = int(command[1])
#         if index in range(len(treasure_chest)):
#             treasure_chest.append(treasure_chest.pop(index))
#     elif action == "Steal":  # else
#         count = int(command[1])
#         if count >= len(treasure_chest):
#             print(", ".join(treasure_chest))
#             treasure_chest = []
#         else:
#             steal_index = len(treasure_chest) - count
#             print(", ".join(treasure_chest[steal_index:]))
#             treasure_chest = treasure_chest[:steal_index]
#     command = input().split()
# if not treasure_chest:  # if treasure_chest == 0
#     print("Failed treasure hunt.")
# else:
#     average = sum(len(item) for item in treasure_chest) / len(treasure_chest)
#     print(f"Average treasure gain: {average:.2f} pirate credits.")
