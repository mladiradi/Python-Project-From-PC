import math

record_sec = float(input())
distance_m = float(input())
meter_per_sec = float(input())

dist_sec = distance_m * meter_per_sec
delay_sec = math.floor(distance_m / 15) * 12.5
result_sec = dist_sec + delay_sec

if result_sec < record_sec:
    print(f'Yes, he succeeded! The new world record is {result_sec:.2f} seconds.')
else:
    print(f'No, he failed! He was {result_sec - record_sec:.2f} seconds slower.')
