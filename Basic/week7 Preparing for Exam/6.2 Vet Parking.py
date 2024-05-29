
days = int(input())
hours = int(input())

price = 0
sum_odd = 0
sum_even = 0
total = 0

for i in range(1, days + 1):
    if i % 2 != 0:
        for ii in range(hours):
            if ii % 2 == 0:
                price += 1
            else:
                price += 1.25
            if ii == hours - 1:
                sum_odd = price
                total += sum_odd
                price = 0
        print(f"Day: {i} - {sum_odd:.2f} leva")
    else:
        for ii in range(hours):
            if ii % 2 == 0:
                price += 2.5
            else:
                price += 1
            if ii == hours - 1:
                sum_even = price
                total += sum_even
                price = 0
        print(f"Day: {i} - {sum_even:.2f} leva")


print(f"Total: {total:.2f} leva")
