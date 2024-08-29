dwarfs = {}
hat_color_count = {}

while True:
    command = input()
    if command == "Once upon a time":
        break

    name, hat_color, physics = command.split(" <:> ")
    physics = int(physics)
    dwarf_key = (name, hat_color)

    if dwarf_key not in dwarfs:
        dwarfs[dwarf_key] = physics
        if hat_color not in hat_color_count:
            hat_color_count[hat_color] = 0
        hat_color_count[hat_color] += 1
    else:
        if dwarfs[dwarf_key] < physics:
            dwarfs[dwarf_key] = physics

dwarf_list = list(dwarfs.items())
for i in range(len(dwarf_list)):
    for j in range(i + 1, len(dwarf_list)):
        (name_i, hat_color_i), physics_i = dwarf_list[i]
        (name_j, hat_color_j), physics_j = dwarf_list[j]

        if physics_i < physics_j or (
                physics_i == physics_j and hat_color_count[hat_color_i] < hat_color_count[hat_color_j]):
            dwarf_list[i], dwarf_list[j] = dwarf_list[j], dwarf_list[i]

for (name, hat_color), physics in dwarf_list:
    print(f"({hat_color}) {name} <-> {physics}")
