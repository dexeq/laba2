def get_odd_numbers():
    return [num for num in range(30) if num % 2 != 0]

# Получаем список нечетных чисел
odd_numbers = get_odd_numbers()

# Находим первое, пятое и последнее значение
first_value = odd_numbers[0]
fifth_value = odd_numbers[4] if len(odd_numbers) > 4 else None
last_value = odd_numbers[-1] if odd_numbers else None

# Вывод значений
print(f"Первое нечетное число: {first_value}")
print(f"Пятое нечетное число: {fifth_value}")
print(f"Последнее нечетное число: {last_value}")