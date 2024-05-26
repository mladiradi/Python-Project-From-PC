length = int(input())
breadth = int(input())
height = int(input())
percent = float(input()) / 100

litre = (length * breadth * height) / 1000
capacity = litre * (1 - percent)

print(capacity)
