import math

record_sec = float(input())
dist_meters = float(input())
sec_per_meter = float(input())

total_sec = dist_meters * sec_per_meter
lag_time = math.floor(dist_meters / 50) * 30
time_total = total_sec + lag_time

if time_total < record_sec:
    print(f"Yes! The new record is {time_total:.2f} seconds.")
else:
    print(f"No! He was {time_total - record_sec:.2f} seconds slower.")
