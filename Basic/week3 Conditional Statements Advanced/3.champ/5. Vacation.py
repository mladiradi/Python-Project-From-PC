budget = float(input())
season = input()

place = ''
location = ''

if budget  <= 1000:
    place = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        budget *= 0.65
    else:
        location = 'Morocco'
        budget *= 0.45
elif 1000 < budget  <= 3000:
    place = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        budget *= 0.8
    else:
        location = 'Morocco'
        budget *= 0.6
else:
    place = 'Hotel'
    budget *= 0.9
    if season == 'Summer':
        location = 'Alaska'
    else:
        location = 'Morocco'

print(f'{location} - {place} - {budget:.2f}')
