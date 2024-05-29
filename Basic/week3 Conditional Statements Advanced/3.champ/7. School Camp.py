vacation = input()
gender = input()
student_num = int(input())
nights_num = int(input())

sport = ''
price_night = 0.0
total_price = 0.0

if vacation == 'Winter':
    if gender == 'girls':
        price_night = 9.6
        sport = 'Gymnastics'
    elif gender == 'boys':
        price_night = 9.6
        sport = 'Judo'
    else:
        price_night = 10
        sport = 'Ski'
elif vacation == 'Spring':
    if gender == 'girls':
        price_night = 7.2
        sport = 'Athletics'
    elif gender == 'boys':
        price_night = 7.2
        sport = 'Tennis'
    else:
        price_night = 9.5
        sport = 'Cycling'
elif vacation == 'Summer':
    if gender == 'girls':
        price_night = 15
        sport = 'Volleyball'
    elif gender == 'boys':
        price_night = 15
        sport = 'Football'
    else:
        price_night = 20
        sport = 'Swimming'

total_price = student_num * price_night * nights_num

if student_num >= 50:
    total_price *= 0.5
elif 20 <= student_num < 50:
    total_price *= 0.85
elif 10 <= student_num < 20:
    total_price *= 0.95

print(f'{sport} {total_price:.2f} lv.')
