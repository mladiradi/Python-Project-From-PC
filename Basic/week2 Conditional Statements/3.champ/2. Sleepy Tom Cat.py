holly = int(input())

norm = 30000
on_work = (365 - holly) * 63
off_work = holly * 127
play_time = on_work + off_work
xtra_H = abs(play_time - norm) // 60
xtra_M = abs(play_time - norm) % 60

if play_time >= norm:
    print("Tom will run away")
    print(f"{xtra_H} hours and {xtra_M} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{xtra_H} hours and {xtra_M} minutes less for play")
