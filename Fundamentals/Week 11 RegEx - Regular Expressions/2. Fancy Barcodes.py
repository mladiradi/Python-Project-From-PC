
import re

n = int(input())

for _ in range(n):
    text = input()
    pattern = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"
    matches = re.match(pattern, text)

    if matches:
        barcode = matches.group(2)
        product_group = ""

        for i in barcode:
            if i.isdigit():
                product_group += i

        if not product_group:
            product_group = "00"

        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")

# # input:
#
# 6
# @###Val1d1teM@###
# @#ValidIteM@#
# ##InvaliDiteM##
# @InvalidIteM@
# @#Invalid_IteM@#
# @#ValiditeM@#
#
# # output:
#
# Product group: 11
# Product group: 00
# Invalid barcode
# Invalid barcode
# Invalid barcode
# Product group: 00
