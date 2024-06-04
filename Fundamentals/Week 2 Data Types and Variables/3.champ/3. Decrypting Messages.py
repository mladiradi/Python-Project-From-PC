
key = int(input())
rows = int(input())

for i in range(rows):
    char = input()
    num = ord(char) + key
    print(chr(num), end="")
