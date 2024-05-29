import math

p_racket = float(input())
n_racket = int(input())
n_sneakers = int(input())

p_sneakers = p_racket / 6

sum_equip = (p_racket * n_racket) + (p_sneakers * n_sneakers)
other_equip = sum_equip * 0.2
total_sum = sum_equip + other_equip

print(f"Price to be paid by Djokovic {math.floor(total_sum / 8)}")
print(f"Price to be paid by sponsors {math.ceil((total_sum * 7) / 8)}")
