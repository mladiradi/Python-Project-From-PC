
contest_data = {}
user_standings = {}

while True:
    line = input()
    if line == "no more time":
        break

    username, contest, points = line.split(" -> ")
    points = int(points)

    if contest not in contest_data:
        contest_data[contest] = {}

    if username in contest_data[contest]:
        if points > contest_data[contest][username]:
            user_standings[username] = user_standings.get(username, 0) + (points - contest_data[contest][username])
            contest_data[contest][username] = points
    else:
        contest_data[contest][username] = points
        user_standings[username] = user_standings.get(username, 0) + points

for contest, participants in contest_data.items():
    sorted_participants = [(user, score) for user, score in participants.items()]

    for i in range(len(sorted_participants)):
        for j in range(i + 1, len(sorted_participants)):
            user1, score1 = sorted_participants[i]
            user2, score2 = sorted_participants[j]
            if score1 < score2 or (score1 == score2 and user1 > user2):
                sorted_participants[i], sorted_participants[j] = sorted_participants[j], sorted_participants[i]

    print(f"{contest}: {len(participants)} participants")
    index = 1
    for user, score in sorted_participants:
        print(f"{index}. {user} <::> {score}")
        index += 1

individuals = [(user, total) for user, total in user_standings.items()]
for i in range(len(individuals)):
    for j in range(i + 1, len(individuals)):
        user1, score1 = individuals[i]
        user2, score2 = individuals[j]
        if score1 < score2 or (score1 == score2 and user1 > user2):
            individuals[i], individuals[j] = individuals[j], individuals[i]

print("Individual standings:")
index = 1
for user, total in individuals:
    print(f"{index}. {user} -> {total}")
    index += 1
