
# https://pastebin.com/2REpE9Xw

items_list = list(map(int, input().split(", ")))
entry_point = int(input())
type_of_items = input()
left_list = []
right_list = []
result = 0
position = ''
if entry_point in range(len(items_list)):
    for left in range(0, entry_point):
        left_list.append(items_list[left])
    for right in range(entry_point + 1, len(items_list)):
        right_list.append(items_list[right])

    if type_of_items == "cheap":
        if min(left_list) <= min(right_list):
            res = [i for i in left_list if i < items_list[entry_point]]
            result = sum(res)
            # result = min(left_list)
            position = "Left"
        else:
            res = [i for i in right_list if i < items_list[entry_point]]
            result = sum(res)
            # result = min(right_list)
            position = "Right"
    elif type_of_items == "expensive":
        if max(left_list) > max(right_list):
            res = [i for i in left_list if i >= items_list[entry_point]]
            result = sum(res)
            # result = sum(left_list)
            position = "Left"
        else:
            res = [i for i in right_list if i >= items_list[entry_point]]
            result = sum(res)
            position = "Right"

print(f"{position} - {result}")
