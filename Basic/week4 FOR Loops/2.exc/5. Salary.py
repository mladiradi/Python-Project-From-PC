n_tabs = int(input())
salary = int(input())

for i in range(0, n_tabs):
    site_name = input()
    if site_name == 'Facebook':
        salary -= 150
    elif site_name == 'Instagram':
        salary -= 100
    elif site_name == 'Reddit':
        salary -= 50
    if salary <= 0:
        print('You have lost your salary.')
        exit()

print(salary)
