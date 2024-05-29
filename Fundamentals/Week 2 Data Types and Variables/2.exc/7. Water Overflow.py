
infusion_num = int(input())

capacity_of_pool = 255
added_liters = 0

for i in range(infusion_num):

    adding_liters = int(input())

    if capacity_of_pool < adding_liters:
        print('Insufficient capacity!')
    else:
        added_liters += adding_liters
        capacity_of_pool -= adding_liters

print(added_liters)


# number_of_lines = int(input())
# tank_capacity = 255
# for line in range(number_of_lines):
#     liters_of_water = int(input())
#     if tank_capacity - liters_of_water < 0:  # no enough capacity for current water
#         print("Insufficient capacity!")
#         continue
#     tank_capacity -= liters_of_water
# print(255 - tank_capacity)
