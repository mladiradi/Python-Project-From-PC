name = input()
seasons_num = int(input())
series_num = int(input())
time_of_serie = float(input())

total_time = 0


serie_adv = time_of_serie * 0.2
sum_serie = time_of_serie + serie_adv
extra_time = seasons_num * 10
tottal_time = (sum_serie * series_num * seasons_num) + extra_time

print(f"Total time needed to watch the {name} series is {tottal_time:.2f} minutes.")
