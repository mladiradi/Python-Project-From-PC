
minute_ctrl = int(input())
sec_ctrl = int(input())
track_m = float(input())
sec_for_100_m = int(input())

ctrl = (minute_ctrl * 60) + sec_ctrl
delay = (track_m / 120) * 2.5
racer_t = (track_m / 100) * sec_for_100_m - delay

if racer_t <= ctrl:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {racer_t:.3f}.")
else:
    print(f"No, Marin failed! He was {racer_t - ctrl:.3f} second slower.")
