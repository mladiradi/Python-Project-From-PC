
# data_base = {}
# while True:
#     data = input()
#     if data == "Lumpawaroo":
#         break
#     if "|" in data:
#         data = input().split("|")
#         side, name = data[0], data[1]
#         if name and side not in data_base:
#             data_base[name] = side
#     elif "->" in data:
#         data = input().split("->")
#         name, side = data[0], data[1]

# ----------------------------------------------------------

force_side_dictionary = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        force_user_is_part_of_the_force = False
        for list_of_force_users in force_side_dictionary.values():
            if force_user in list_of_force_users:
                force_user_is_part_of_the_force = True
                break
        if not force_user_is_part_of_the_force:
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = []
            force_side_dictionary[force_side].append(force_user)

    elif "->" in command:  # else:
        force_user, force_side = command.split(" -> ")
        for list_of_force_users in force_side_dictionary.values():
            if force_user in list_of_force_users:
                list_of_force_users.remove(force_user)
                break
        if force_side not in force_side_dictionary.keys():
            force_side_dictionary[force_side] = []
        force_side_dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()

for force_side, list_of_force_users in force_side_dictionary.items():
    if list_of_force_users: #if len(list_of_force_users) > 0
        print(f"Side: {force_side}, Members: {len(list_of_force_users)}")
        for force_user in list_of_force_users:
            print(f"! {force_user}")

# ------------------------------------------------------------------------

# # input:
#
# Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Lighter
# DCay -> Lighter
# Lumpawaroo
#

# # result:
#
# Ivan Ivanov joins the Lighter side!
# DCay joins the Lighter side!
# Side: Lighter, Members: 3
# ! Royal
# ! Ivan Ivanov
# ! DCay
