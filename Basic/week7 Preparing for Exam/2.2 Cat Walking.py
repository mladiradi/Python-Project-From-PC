
minute_day = int(input())
walk_num_day = int(input())
eat_calo_day = int(input())

total_min = minute_day * walk_num_day
burn_calo = total_min * 5
left_calo = eat_calo_day / 2

if burn_calo >= left_calo:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burn_calo}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burn_calo}.")
