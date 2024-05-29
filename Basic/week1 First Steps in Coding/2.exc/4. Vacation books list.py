num_pages = int(input())
pages_per_hour = int(input())
days = int(input())

book_hours = num_pages / pages_per_hour
hours_per_day = book_hours / days

print(int(hours_per_day))
