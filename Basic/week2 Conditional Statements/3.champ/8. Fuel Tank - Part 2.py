type_f = str.lower(input())
ltr_f = float(input())
card = str.lower(input())

benz = ltr_f * 2.22
dsl = ltr_f * 2.33
gas = ltr_f * 0.93

if type_f == 'gasoline' or type_f == 'diesel' or type_f == 'gas':
    if card == 'yes':
        benz = ltr_f * (2.22 - 0.18)
        dsl = ltr_f * (2.33 - 0.12)
        gas = ltr_f * (0.93 - 0.08)
    if 20.0 < ltr_f <= 25.0:
        benz *= 0.92
        dsl *= 0.92
        gas *= 0.92
    if ltr_f > 25.0:
        benz *= 0.9
        dsl *= 0.9
        gas *= 0.9

if type_f == 'gasoline':
    print(f'{benz:.2f} lv.')
elif type_f == 'diesel':
    print(f'{dsl:.2f} lv.')
else:
    print(f'{gas:.2f} lv.')
