nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_p = (nylon + 2) * 1.5
paint_p = (paint + (paint * 0.1)) * 14.5
thinner_p = thinner * 5
bags = 0.4

sum_m = nylon_p + paint_p + thinner_p + bags
total_sum = sum_m + ((sum_m * 0.3) * hours)

print(total_sum)
