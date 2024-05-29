
bitcoin_n = int(input())
yuan_n = float(input())
commission_p = float(input())

bit_l = bitcoin_n * 1168
yuan_l = (yuan_n * 0.15) * 1.76
sum_euro = (bit_l + yuan_l) / 1.95
commission = (sum_euro * commission_p) / 100
total = sum_euro - commission

print(f'{total:.2f}')
