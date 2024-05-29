
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while True:
    command = input()
    if command == "Finish":
        break
    else:
        movie_name = command
        capacity = int(input())
        full_places = 0

        while True:
            command2 = input()
            if command2 == "End":
                break
            elif command2 == "student":
                student_tickets += 1
            elif command2 == "standard":
                standard_tickets += 1
            elif command2 == "kid":
                kids_tickets += 1

            full_places += 1
            total_tickets += 1

            if capacity == full_places:
                break

        print(f"{movie_name} - {(full_places / capacity) * 100:.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kids_tickets / total_tickets) * 100:.2f}% kids tickets.")


#
# total_tickets = 0
# student_t = 0
# standard_t = 0
# kid_t = 0
#
# while True:
#     text = input()
#     if text == "Finish":
#         print(f"Total tickets: {total_tickets}")
#         print(f"{(student_t / total_tickets) * 100:.2f}% student tickets.")
#         print(f"{(standard_t / total_tickets) * 100:.2f}% standard tickets.")
#         print(f"{(kid_t / total_tickets) * 100:.2f}% kids tickets.")
#         break
#     else:
#         movie_name = text
#         seats = int(input())
#         counter = 0
#         for i in range(seats):
#             type_ticket = input()
#
#             if type_ticket == "student":
#                 student_t += 1
#             elif type_ticket == "standard":
#                 standard_t += 1
#             elif type_ticket == "kid":
#                 kid_t += 1
#             elif type_ticket == "End" or seats == total_tickets:
#                 break
#             counter += 1
#             total_tickets += 1
#
#         print(f"{movie_name} - {(counter / seats) * 100:.2f}% full.")
