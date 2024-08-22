
words = input().split(", ")
text = input()

for word in words:
    while word in text:
        text = text.replace(word, "*" * len(word))

print(text)

# # input:
#
# Linux, Windows
# It is not Linux, it is GNU/Linux. Linux is merely the kernel,
# while GNU adds the functionality.
# Therefore we owe it to them by calling the OS GNU/Linux!
# Sincerely, a Windows client


# result:

# It is not *****, it is GNU/*****. ***** is merely the kernel,
# while GNU adds the functionality.
# Therefore we owe it to them by calling the OS GNU/*****!
# Sincerely, a ******* client
