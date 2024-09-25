
import re

furniture = []
total_price = 0
text = input()
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"

while text != "Purchase":
    match = re.search(pattern, text)
    if match:
        stock, price, quantity = match.groups()
        furniture.append(stock)
        total_price += float(price) * int(quantity)

    text = input()

print("Bought furniture:")
for i in furniture:
    print(i)

print(f"Total money spend: {total_price:.2f}")

# # input:
#
#     >> Sofa << 312.23!3
#     >> TV << 300!5
#     > Invalid <<!5
#     Purchase

# # output:
#
# Bought furniture:
# Sofa
# TV
# Total money spend: 2436.69
