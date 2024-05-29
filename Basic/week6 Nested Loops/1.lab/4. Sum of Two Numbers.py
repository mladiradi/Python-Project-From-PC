
start_interval = int(input())
stop_interval = int(input())
magic_number = int(input())

count = 0
quiter = 0

for i in range(start_interval, stop_interval + 1):
    if quiter == 1:
        break
    for ii in range(start_interval, stop_interval + 1):
        sumer = i + ii
        count += 1

        if sumer == magic_number:
            quiter += 1
            print(f'Combination N:{count} ({i} + {ii} = {sumer})')
            break

if quiter != 1:
    print(f'{count} combinations - neither equals {magic_number}')
