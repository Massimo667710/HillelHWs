total_seconds = int(input('Введіть кількість секунд (від 0 до 8639999): '))

if 0 <= total_seconds < 8640000:
    days, seconds_left = divmod(total_seconds, 86400)
    hours, seconds_left = divmod(seconds_left, 3600)
    minutes, seconds = divmod(seconds_left, 60)
    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_word = "дні"
    else:
        day_word = "днів"

    print(f'{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
else:
    print('Введене число повинно буди від в до 8639999. ')