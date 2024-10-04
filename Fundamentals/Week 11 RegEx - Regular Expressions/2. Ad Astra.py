
import re

text = input()
pattern = r'(#|\|)([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,4})\1'
# калориите да са макс 10000(невкл. или 9999), т.е. 4 числа или (\d{от 1, до 4})

matches = re.finditer(pattern, text)

calories_counter = 0
food_item = []

for match in matches:
    item = match.group(2)
    expire_date = match.group(3)
    calories = int(match.group(4))

    calories_counter += calories
    food_item.append([item, expire_date, calories])

days = calories_counter // 2000
print(f"You have food to last you for: {days} days!")

for item, expire_date, calories in food_item:
    print(f'Item: {item}, Best before: {expire_date}, Nutrition: {calories}')


# # input:
#
# # Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|

# # output:
#
# You have food to last you for: 2 days!
# Item: Bread, Best before: 19/03/21, Nutrition: 4000
# Item: Apples, Best before: 08/10/20, Nutrition: 200
# Item: Carrots, Best before: 06/08/20, Nutrition: 500

#Bread#19/03/21#400000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|
