
def decad_group(nums):
    group_border = 10
    rest = []

    while nums:
        group = [num for num in nums if num <= group_border]
        nums = [num for num in nums if num > group_border]
        rest.append(f"Group of {group_border}'s: {group}")
        group_border += 10

    for index in rest:
        print(index)


seq_num = list(map(int, input().split(', ')))
decad_group(seq_num)
