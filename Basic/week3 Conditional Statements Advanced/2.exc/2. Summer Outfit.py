degree = int(input())
atc = str.lower(input())  #Around The Clock

outfit = ''
shoes = ''

if 10 <= degree <= 18:
    if atc == 'morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif atc == 'afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < degree <= 24:
    if atc == 'morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif atc == 'afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif degree >= 25:
    if atc == 'morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif atc == 'afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'
print(f"It's {degree} degrees, get your {outfit} and {shoes}.")
