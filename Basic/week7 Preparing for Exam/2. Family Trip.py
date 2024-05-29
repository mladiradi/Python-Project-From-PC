
budget = float(input())
nights_num = int(input())
price_night = float(input())
percent_spent = int(input())

if nights_num > 7:
    price_night *= 0.95

final_price = nights_num * price_night + (budget * percent_spent) / 100

if budget >= final_price:
    print(f"Ivanovi will be left with {budget - final_price:.2f} leva after vacation.")
else:
    print(f"{final_price - budget:.2f} leva needed.")
