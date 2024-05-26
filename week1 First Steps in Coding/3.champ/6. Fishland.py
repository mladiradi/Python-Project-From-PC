mack_p = float(input())
sprat_p = float(input())
bonito_kg = float(input())
trach_kg = float(input())
mussels_kg = int(input())

bonito_p = (mack_p * (1 + 0.6)) * bonito_kg
trach_p = (sprat_p * (1 + 0.8)) * trach_kg
mussels_p = 7.5 * mussels_kg

total = bonito_p + trach_p + mussels_p

print('%.2f' % total)
