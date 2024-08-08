resources_dict = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())

    if resource not in resources_dict.keys():
        resources_dict[resource] = 0
    resources_dict[resource] += quantity

for resource, quantity in resources_dict.items():
    print(f"{resource} -> {quantity}")

# # input:
#
# gold
# 155
# silver
# 10
# copper
# 17
# gold
# 15
# stop

# # result:
#
# gold -> 170
# silver -> 10
# copper -> 17
