
class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
line = input()
while line != "Stop":
    tokens = line.split(" ")
    email = Email(tokens[0], tokens[1], tokens[2])
    emails.append(email)
    line = input()
send_emails = [int(x) for x in input().split(", ")]
for x in send_emails:
    emails[x].send()
for email in emails:
    print(email.get_info())


# Peter John Hi,John
# John Peter Hi,Peter!
# Katy Lilly Hello,Lilly
# Stop
# 0, 2

# # result:
# # Peter says to John: Hi,John. Sent: True
# # John says to Peter: Hi,Peter!. Sent: False
# # Katy says to Lilly: Hello,Lilly. Sent: True


# # logic 2
#
# emails = []
#
# while True:
#     data = input().split(" ")
#
#     if data[0] == "Stop":
#         break
#
#     sender, receiver, content = data
#     current_email = Email(sender, receiver, content)
#     emails.append(current_email)
#
# indices = list(map(int, input().split(", ")))
# for index in indices:
#     emails[index].send()
#
# for email in emails:
#     print(email.get_info())

# # logic 3
# emails = []
#
# line = input()
# while line != "Stop":
#     tokens = line.split(" ")
#     sender = tokens[0]
#     receiver = tokens[1]
#     content = tokens[2]
#     email = Email(sender, receiver, content)
#     emails.append(email)
#     line = input()
#
# send_emails = list(map(lambda x: int(x), input().split(", ")))
#
# for x in send_emails:
#     emails[x].send()
#
# for email in emails:
#     print(email.get_info())
