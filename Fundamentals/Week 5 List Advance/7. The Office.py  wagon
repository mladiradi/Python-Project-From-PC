#
# def happy_checker(white_collar_worker, factor):
#     happy_fac = [curnt_value * factor for curnt_value in white_collar_worker]
#     ave_happy = sum(happy_fac) / len(happy_fac)
#     counter_of_happyness = sum(num >= ave_happy for num in happy_fac)
#     total_counter_of_happynes_of_employes = len(happy_fac)
#     meisig = 'happy' if counter_of_happyness >= total_counter_of_happynes_of_employes / 2 else 'not happy'
#     return f'Score: {counter_of_happyness}/{total_counter_of_happynes_of_employes}. Employees are {meisig}!'
#
#
# employee_list = list(map(int, input().split(" ")))
# happy_factor = int(input())
# result = happy_checker(employee_list, happy_factor)
# print(result)

emplo = input().split(" ")
happ_fac = int(input())

emplo = list(map(lambda x: int(x) * happ_fac, emplo))
filt = list(filter(lambda x: x >= (sum(emplo) / len(emplo)), emplo))

if len(filt) >= len(emplo) / 2:
    print(f'Score: {len(filt)}/{len(emplo)}. Employees are happy!')
else:
    print(f'Score: {len(filt)}/{len(emplo)}. Employees are not happy!')
