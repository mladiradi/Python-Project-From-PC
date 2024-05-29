
contract_years = str.lower(input())
type_contract = str.lower(input())
mobile_net_add = str.lower(input())
month_num = int(input())

if type_contract == "small":
    if contract_years == "one":
        price = 9.98
    else:
        price = 8.58
elif type_contract == "middle":
    if contract_years == 'one':
        price = 18.99
    else:
        price = 17.09
elif type_contract == "large":
    if contract_years == "one":
        price = 25.98
    else:
        price = 23.59
else:
    if contract_years == "one":
        price = 35.99
    else:
        price = 31.79

if mobile_net_add == "yes":
    if price <= 10.00:
        price += 5.5
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85

total = month_num * price
if contract_years == "two":
    total *= 0.9625

print(f"{total:.2f} lv.")
