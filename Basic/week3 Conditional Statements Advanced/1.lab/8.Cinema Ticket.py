day = str.lower(input())

if day == 'monday' or day == 'tuesday' or day == 'friday':
    print(12)
elif day == 'wednesday' or day == 'thursday':
    print(14)
else:
    print(16)
