
n = int(input())
library = {}

for _ in range(n):
    text = input().split("<->")
    plant, rarity = text[0], text[1]
    if plant not in library:
        library[plant] = {'rarity': rarity, 'ratings': []}
    else:
        library[plant]['rarity'] = rarity

while True:
    text = input()
    if text == "Exhibition":
        break
    text = text.split(": ")
    action = text[0]
    if action == "Rate":
        elements = text[1].split(" - ")
        plant = elements[0]
        rating = int(elements[1])
        if plant in library:
            library[plant]['ratings'].append(rating)
        else:
            print("error")

    elif action == "Update":
        elements = text[1].split(" - ")
        plant = elements[0]
        new_rarity = elements[1]
        if plant in library:
            library[plant]['rarity'] = new_rarity
        else:
            print("error")

    elif action == "Reset":
        elements = text[1].split(" - ")
        plant = elements[0]
        if plant in library:
            library[plant]['ratings'] = []
        else:
            print("error")
print("Plants for the exhibition:")
for plant, info in library.items():
    if info['ratings']:
        average_rating = sum(info['ratings']) / len(info['ratings'])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {info['rarity']}; Rating: {average_rating:.2f}")

# # input:
#
# 3
# Arnoldii<->4
# Woodii<->7
# Welwitschia<->2
# Rate: Woodii - 10
# Rate: Welwitschia - 7
# Rate: Arnoldii - 3
# Rate: Woodii - 5
# Update: Woodii - 5
# Reset: Arnoldii
# Exhibition
#
# # 2:
#
# 2
# Candelabra<->10
# Oahu<->10
# Rate: Oahu - 7
# Rate: Candelabra - 6
# Exhibition


# # output:
#
# Plants for the exhibition:
# - Arnoldii; Rarity: 4; Rating: 0.00
# - Woodii; Rarity: 5; Rating: 7.50
# - Welwitschia; Rarity: 2; Rating: 7.00
#
# # 2:
#
# Plants for the exhibition:
# - Candelabra; Rarity: 10; Rating: 6.00
# - Oahu; Rarity: 10; Rating: 7.00
