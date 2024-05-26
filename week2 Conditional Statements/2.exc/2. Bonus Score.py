nom = int(input())
bon = 0

if nom <= 100:
    bon += 5
elif 100 < nom <= 1000:
    bon = nom * 0.2
else:
    bon = nom * 0.1

if nom % 2 == 0:
    bon += 1
elif nom % 10 == 5:
    bon += 2

print(bon)
print(nom + bon)
