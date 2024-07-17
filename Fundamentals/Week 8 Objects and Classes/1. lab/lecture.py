# class Pero:
#     def __init__(selfie, name, age):
#         selfie.name = name
#         selfie.age = age
#
#     def intro(selfie):
#         print(f"{selfie.name} suck my {selfie.age} years old cock.")
#
#
# per1 = Pero(input(), input())
# # per1= Pero("Poli", 55)
# per1.intro()

# class Person:
#     def __init__(self, f_name, s_name, age):
#         self.one_name = f_name
#         self.two_name = s_name
#         self.n_age = age - 10
#
#     def real_name(self):
#         print(f'My name is {self.one_name} and my second name is {self.two_name} i am {self.n_age} years old.')
#
#
# name_1 = input()
# name_2 = input()
# ages = int(input())
# after = Person(name_1, name_2, ages)
# after.real_name()

class Party:
    def __init__(self):
        self.people = []


party = Party()
line = input()
while line != "End":
    party.people.append(line)
    line = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")

# class Person:
#     species = "mammal"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def pirint(self):
#         print(f'I am mammal !')
#
#
# me = Person("Peter", 25)
# you = Person("John", 44)
# # me.species = "mammal"
# # you.species = "mammal"
# you.pirint()

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#
# me = Person("Peter", "Johnson", 64)
# print(me.get_full_name())  # Peter Johnson

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

