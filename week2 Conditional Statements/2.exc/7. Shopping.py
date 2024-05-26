budget = float(input())
GPU_n = int(input())
CPU_n = int(input())
RAM_n = int(input())

GPU_price = 250
GPU_total = GPU_n * GPU_price
CPU_total = CPU_n * (GPU_total * (1 - 0.65))
RAM_total = RAM_n * (GPU_total * (1 - 0.9))
total_sum = GPU_total + CPU_total + RAM_total

if GPU_n > CPU_n:
    #total_sum = total_sum * (1 - 0.15)
    total_sum *= 0.85
if budget >= total_sum:
    print(f'You have {budget - total_sum:.2f} leva left!')
else:
    print(f'Not enough money! You need {total_sum - budget:.2f} leva more!')
