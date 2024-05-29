exam_h = int(input())
exam_m = int(input())
arri_h = int(input())
arri_m = int(input())

arri_s = arri_h * 60 + arri_m
exam_s = exam_h * 60 + exam_m
gap = exam_s - arri_s
stat = ''

if 0 <= gap <= 30:
    stat = 'On Time'
elif gap > 30:
    stat = 'Early'
else:
    stat = 'Late'
print(stat)

if gap < 0:
    stat_2 = 'after'
else:
    stat_2 = 'before'

gap = abs(gap)

if gap != 0:
    if 60 <= gap < 70 or gap % 60 <= 0:
        print(f'{gap // 60}:0{gap % 60} hours {stat_2} the start')
        exit()
    if gap < 60:
        print(f'{gap} minutes {stat_2} the start')
        exit()
    else:
        print(f'{gap // 60}:{gap % 60} hours {stat_2} the start')
