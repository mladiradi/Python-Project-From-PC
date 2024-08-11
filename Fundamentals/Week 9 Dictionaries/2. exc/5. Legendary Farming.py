
materials = {"shards": 0, "fragments": 0, "motes": 0}
winner_item = False

while not winner_item:
    items = input().split()
    for index in range(0, len(items), 2):
        value = int(items[index])
        key = items[index + 1].lower()
        if key not in materials.keys():
            materials[key] = 0
        materials[key] += value
        if materials["shards"] >= 250:
            materials["shards"] -= 250
            print("Shadowmourne obtained!")
            winner_item = True
        elif materials["fragments"] >= 250:
            materials["fragments"] -= 250
            print("Valanyr obtained!")
            winner_item = True
        elif materials["motes"] >= 250:
            materials["motes"] -= 250
            print("Dragonwrath obtained!")
            winner_item = True
        if winner_item:
            break

for key, value in materials.items():
    print(f"{key}: {value}")

# # input:
#
# 3 Motes 5 stones 5 Shards
# 6 leathers 255 fragments 7 Shards

# # result:
#
# Valanyr obtained!
# shards: 5
# fragments: 5
# motes: 3
# stones: 5
# leathers: 6
