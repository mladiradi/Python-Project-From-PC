mont = input()
nigh = int(input())

stud_p = 0
apar_p = 0

if mont == 'May' or mont == 'October':
    stud_p = nigh * 50
    apar_p = nigh * 65
    if 7 < nigh <= 14:
        stud_p *= 0.95
    elif nigh > 14:
        stud_p *= 0.7
        apar_p *= 0.9
elif mont == 'June' or mont == 'September':
    stud_p = nigh * 75.2
    apar_p = nigh * 68.7
    if nigh > 14:
        stud_p *= 0.8
        apar_p *= 0.9
elif mont == 'July' or mont == 'August':
    stud_p = nigh * 76
    apar_p = nigh * 77
    if nigh > 14:
        apar_p *= 0.9

print(f'Apartment: {apar_p:.2f} lv.')
print(f'Studio: {stud_p:.2f} lv.')
