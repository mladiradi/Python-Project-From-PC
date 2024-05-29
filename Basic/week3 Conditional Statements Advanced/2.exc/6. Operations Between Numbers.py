n1 = int(input())
n2 = int(input())
oper = input()

sum = 0

if n1 == 0:
    print(f'Cannot divide {n2} by zero')
    exit()
elif n2 == 0:
    print(f'Cannot divide {n1} by zero')
    exit()

if oper == '+':
    sum = n1 + n2
elif oper == '-':
    sum = n1 - n2
elif oper == '*':
    sum = n1 * n2
elif oper == '/':
    sum = n1 / n2
    print(f'{n1} {oper} {n2} = {sum:.2f}')
    exit()
elif oper == '%':
    sum = n1 % n2
    print(f'{n1} {oper} {n2} = {sum}')
    exit()

if sum % 2 == 0:
    print(f'{n1} {oper} {n2} = {sum} - even')
else:
    print(f'{n1} {oper} {n2} = {sum} - odd')
