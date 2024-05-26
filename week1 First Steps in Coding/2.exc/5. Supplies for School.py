n_pens = int(input()) * 5.8
n_markers = int(input()) * 7.2
l_chemicals = int(input()) * 1.2
perc_discount = int(input()) / 100

sum = n_pens + n_markers + l_chemicals
final_sum = sum - (sum * perc_discount)

print(final_sum)
