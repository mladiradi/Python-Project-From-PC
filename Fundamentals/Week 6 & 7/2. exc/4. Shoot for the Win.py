
targets_list = list(map(int, input().split()))
shot_targets = 0

while True:
    command = input()
    if command == 'End':
        print(f"Shot targets: {shot_targets} -> {' '.join(map(str, targets_list))}")
        break

    shot_index = int(command)
    if shot_index in range(len(targets_list)):
        current_number = targets_list[shot_index]
        for i in range(len(targets_list)):
            if targets_list[i] != -1:
                if targets_list[i] > current_number:
                    targets_list[i] -= current_number
                else:
                    targets_list[i] += current_number
        targets_list[shot_index] = -1
        shot_targets += 1

# 24 50 36 70
# 0
# 4
# 3
# 1
# End


# # result:
# Shot targets 3 -> -1 -1 130 -1
