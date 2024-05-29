top = int(input())

start_j = top - 30

fail_count = 0
total_count = 0

while True:
    jump = int(input())
    total_count += 1
    if jump > start_j:
        if start_j >= top:
            print(f"Tihomir succeeded, he jumped over {start_j}cm after {total_count} jumps.")
            break
        start_j += 5
        fail_count = 0
    else:
        fail_count += 1
        if fail_count == 3:
            print(f"Tihomir failed at {start_j}cm after {total_count} jumps.")
            break
