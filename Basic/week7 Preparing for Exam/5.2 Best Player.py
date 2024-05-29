
name = ''
total_goals = 0

while True:
    text = input()
    if text == 'END':
        break
    goals = int(input())
    if goals > total_goals:
        total_goals = goals
        name = text
        goals = 0
    if total_goals >= 10:
        break

print(f"{name} is the best player!")
if total_goals >= 3:
    print(f"He has scored {total_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {total_goals} goals.")
    