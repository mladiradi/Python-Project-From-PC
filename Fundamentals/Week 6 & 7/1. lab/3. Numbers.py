
numbers = list(map(int, input().split()))
ave_num = sum(numbers) / len(numbers) if numbers else 0  # (тоя if е като филтър за входа от данни)
# average na SUM of NUMBERS - така ще намерим средното на ... нумберс


greater_num_ave_sum = [num for num in numbers if num > ave_num]

if greater_num_ave_sum:
    top_numbers = sorted(greater_num_ave_sum, reverse=True)[:5]  # след сортирането ще вземе само последните 5 числа (който са най-големите)
                                                                    # и после ще ги ревърсне

    print(' '.join(map(str, top_numbers)))
else:
    print('No')
