
aero_comp_name = input()
adult_n_tickets = int(input())
kids_n_tickets = int(input())
net_adult_p = float(input())
tax_p = float(input())

net_kids_p = net_adult_p * 0.3
total = (adult_n_tickets * (tax_p  + net_adult_p)) + (kids_n_tickets * (tax_p + net_kids_p))
profit = total * 0.2

print(f"The profit of your agency from {aero_comp_name} tickets is {profit:.2f} lv.")
