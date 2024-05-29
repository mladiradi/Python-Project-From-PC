import sys
nn = int(input())

OddSum = 0.0
OddMin = sys.maxsize
OddMax = -sys.maxsize
EvenSum = 0.0
EvenMin = sys.maxsize
EvenMax = -sys.maxsize

for i in range(0, nn):
    n = float(input())
    if i % 2 != 0:
        EvenSum += n
        if n > EvenMax:
            EvenMax = n
        if n < EvenMin:
            EvenMin = n
    else:
        OddSum += n
        if n > OddMax:
            OddMax = n
        if n < OddMin:
            OddMin = n

print(f'OddSum={OddSum:.2f},')
if OddMin != 0.0 and OddMin != sys.maxsize:
    print(f'OddMin={OddMin:.2f},')
else:
    print('OddMin=No,')
if OddMax != 0.0 and OddMax != -sys.maxsize:
    print(f'OddMax={OddMax:.2f},')
else:
    print('OddMax=No,')
print(f'EvenSum={EvenSum:.2f},')
if EvenMin != 0.0 and EvenMin != sys.maxsize:
    print(f'EvenMin={EvenMin:.2f},')
else:
    print('EvenMin=No,')
if EvenMax != 0.0 and EvenMax != -sys.maxsize:
    print(f'EvenMax={EvenMax:.2f}')
else:
    print('EvenMax=No')
