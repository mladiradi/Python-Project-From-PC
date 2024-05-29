
name_movie = input()
days_num = int(input())
tickets_num = int(input())
price_ticket = float(input())
percent = int(input())

sum_tickets = tickets_num * price_ticket
sum_profit = sum_tickets * days_num
cinema_profit = (sum_profit * percent) / 100
studio_profit = sum_profit - cinema_profit

print(f"The profit from the movie {name_movie} is {studio_profit:.2f} lv.")
