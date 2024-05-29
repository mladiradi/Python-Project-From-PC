
lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())

helmets = lost_fights // 2
sword = lost_fights // 3
shield = lost_fights // (2 * 3)
armour = shield // 2

bill = helmets * helmet_price + sword * sword_price \
           + shield * shield_price + armour * armour_price

print(f"Gladiator expenses: {bill:.2f} aureus")

#        https://pastebin.com/eBJwqnw8

#
# fights_num = int(input())
# helmet_p = float(input())
# sword_p = float(input())
# shield_p = float(input())
# armour_p = float(input())
#
# helmets = 0
# swords = 0
# shields = 0
# armours = 0
#
# for fight in range(1, fights_num +1):
#
#     if fight % 2 == 0:
#         helmets += 1
#
#     if fight % 3 == 0:
#         swords += 1
#         if fight % 2 == 0:
#             shields += 1
#             if shields % 2 == 0:
#                 armours += 1
#
# total_price = (helmets * helmet_p) + (swords * sword_p) \
#             + (shields * shield_p) + (armours * armour_p)
#
# print(f"Gladiator expenses: {total_price:.2f} aureus")
