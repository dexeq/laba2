def calc_age():
    # Запрашиваем дату рождения
    birth_date_str = input("Введите дату рождения (дд/мм/гггг): ")
    # Запрашиваем сегодняшнюю дату
    today_date_str = input("Введите сегодняшнюю дату (дд/мм/гггг): ")

    # Преобразуем введенные строки в списки целых чисел
    try:
        birth_day, birth_month, birth_year = map(int, birth_date_str.split('/'))
        today_day, today_month, today_year = map(int, today_date_str.split('/'))
    except ValueError:
        print("Неверный формат даты. Пожалуйста, используйте формат дд/мм/гггг.")
        return

    # Вычисляем возраст
    age = today_year - birth_year

    # Проверяем, был ли день рождения в этом году
    if (today_month, today_day) < (birth_month, birth_day):
        age -= 1

    print(f"Ваш возраст: {age} лет.")

# Вызов функции
calc_age()