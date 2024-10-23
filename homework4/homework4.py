def generate_random_numbers(n, min_val, max_val):
    numbers = []
    for _ in range(n):
        numbers.append((hash(str(_)) % (max_val - min_val + 1)) + min_val)
    return numbers

def find_multiples():
    # Генерируем случайный список чисел > 10
    numbers = generate_random_numbers(10, 0, 200)
    
    print(f"Сгенерированные числа: {numbers}")
    
    # Запрашиваем у пользователя цифру X
    try:
        x = int(input("Введите цифру X (от 1 до 9): "))
        if x < 1 or x > 9:
            print("Пожалуйста, введите цифру от 1 до 9.")
            return
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите целое число.")
        return

    # Используем лямбда-функцию для поиска кратных чисел
    multiples = list(filter(lambda num: num % x == 0, numbers))
    
    # Отображаем найденные числа
    if multiples:
        print(f"Числа, кратные {x}: {multiples}")
    else:
        print(f"Нет чисел, кратных {x}.")

# Вызов функции
find_multiples()