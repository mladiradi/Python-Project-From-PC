
rooms_num = int(input())
empty_chairs = 0
flag = False

for room in range(1, rooms_num + 1):
    chairs, visitors = input().split()
    diff = abs(int(visitors)-len(chairs))
    if len(chairs) < int(visitors):
        print(f'{diff} more chairs needed in room {room}')
        flag = True
    else:
        empty_chairs += diff
if not flag:
    print(f'Game On, {empty_chairs} free chairs left')
