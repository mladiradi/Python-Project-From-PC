
def merge(datas, start_index, end_index):
    start_index = max(0, start_index)
    end_index = min(len(datas) - 1, end_index)

    if start_index < end_index:
        merged = ''.join(datas[start_index:end_index + 1])
        datas[start_index:end_index + 1] = [merged]


def divide(datas, index, partitions):
    element = datas[index]
    part_length = len(element) // partitions

    divided_parts = []
    start = 0

    for i in range(partitions):
        if i == partitions - 1:
            divided_parts.append(element[start:])
        else:
            divided_parts.append(element[start:start + part_length])
            start += part_length
    datas[index:index + 1] = divided_parts


def process_commands(datas, commandos):

    for commando in commandos:
        parts = commando.split()

        if parts[0] == "merge":
            start_index = int(parts[1])
            end_index = int(parts[2])
            merge(datas, start_index, end_index)

        elif parts[0] == "divide":
            index = int(parts[1])
            partitions = int(parts[2])
            divide(data, index, partitions)

    return datas


data = input().split()
commands = []

while True:
    command = input()

    if command == '3:1':
        break

    commands.append(command)


result = process_commands(data, commands)
print(' '.join(result))
