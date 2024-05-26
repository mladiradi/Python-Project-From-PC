t1 = int(input())
t2 = int(input())
t3 = int(input())

total = t1 + t2 + t3
min = total // 60
sec = total % 60

if sec < 10:
    print(f'{min}:0{sec}')
else:
    print(f'{min}:{sec}')
