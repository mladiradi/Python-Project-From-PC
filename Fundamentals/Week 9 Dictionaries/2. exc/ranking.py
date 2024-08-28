
contests = {}
while True:
    line = input()
    if line == "end of contests":
        break
    contest, password = line.split(":")
    contests[contest] = password

submissions = {}
while True:
    line = input()
    if line == "end of submissions":
        break
    contest, password, username, points = line.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in submissions:
            submissions[username] = {}
        if contest not in submissions[username]:
            submissions[username][contest] = 0

        if points > submissions[username][contest]:
            submissions[username][contest] = points

total_points = {}
for user, contests in submissions.items():
    total_points[user] = sum(contests.values())

best_candidate = None
best_points = 0
for user, points in total_points.items():
    if points > best_points:
        best_points = points
        best_candidate = user

print(f"Best candidate is {best_candidate} with total {best_points} points.")
print("Ranking:")

usernames = list(submissions.keys())
usernames.sort()

for user in usernames:
    print(user)

    contest_list = list(submissions[user].items())

    for i in range(len(contest_list)):
        for j in range(i + 1, len(contest_list)):
            if contest_list[i][1] < contest_list[j][1]:
                contest_list[i], contest_list[j] = contest_list[j], contest_list[i]

    for contest, points in contest_list:
        print(f"#  {contest} -> {points}")


#
# contests = {}
#
# while True:
#     line = input().strip()
#     if line == "end of contests":
#         break
#     contest, password = line.split(":")
#     contests[contest] = password
#
# # Step 2: Parse submissions
# submissions = {}
#
# while True:
#     line = input().strip()
#     if line == "end of submissions":
#         break
#     contest, password, username, points = line.split("=>")
#     points = int(points)
#
#     # Validate contest and password
#     if contest in contests and contests[contest] == password:
#         if username not in submissions:
#             submissions[username] = {}
#         if contest not in submissions[username]:
#             submissions[username][contest] = 0
#
#         # Update points if the new points are higher
#         if points > submissions[username][contest]:
#             submissions[username][contest] = points
#
# # Step 3: Calculate total points for each user
# total_points = {user: sum(contests.values()) for user, contests in submissions.items()}
#
# # Step 4: Find the best candidate
# best_candidate = max(total_points, key=total_points.get)
# best_points = total_points[best_candidate]
#
# # Step 5: Print results
# print(f"Best candidate is {best_candidate} with total {best_points} points.")
# print("Ranking:")
#
# # Sort users by name
# for user in sorted(submissions):
#     print(user)
#     # Sort contests by points using an inline key function
#     sorted_contests = sorted(submissions[user].items(), key=lambda entry: -entry[1])
#     for contest, points in sorted_contests:
#         print(f"#  {contest} -> {points}")



