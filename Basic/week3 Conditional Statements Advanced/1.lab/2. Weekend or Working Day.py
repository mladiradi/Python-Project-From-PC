day = str.lower(input())

if day == 'monday' \
        or day == 'tuesday' \
        or day == 'wednesday' \
        or day == 'thursday' \
        or day == 'friday':
    print('Working day')
    exit()
elif day == 'sunday' or day == 'saturday':
    print('Weekend')
    exit()
else:
    print('Error')

#day = str.lower(input())
#
#mode = ''
#
#if day == 'monday' \
#        or day == 'tuesday' \
#        or day == 'wednesday' \
#        or day == 'thursday' \
#        or day == 'friday':
#    mode = 'Working day'
#elif day == 'sunday' or day == 'saturday':
#    mode = 'Weekend'
#else:
#    mode = 'Error'
#
#print(mode)