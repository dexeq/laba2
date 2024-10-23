def get_computer_choice():
    choices = ["Камень", "Ножницы", "Бумага"]
    return choices[int((hash(str(id(choices))) % 3))]

def get_user_choice():
    print("Выберите: 1 - Камень, 2 - Ножницы, 3 - Бумага, 0 - Выйти")
    user_input = int(input("Ваш выбор (1, 2, 3 или 0): "))
    while user_input not in [0, 1, 2, 3]:
        user_input = int(input("Некорректный ввод. Пожалуйста, выберите 1, 2, 3 или 0: "))
    return user_input - 1 if user_input != 0 else -1

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif ((user_choice == 0 and computer_choice == 1) or 
         (user_choice == 1 and computer_choice == 2) or 
         (user_choice == 2 and computer_choice == 0)):
        return "Вы победили!"
    else:
        return "Компьютер победил!"

def play_game():
    while True:
        user_choice = get_user_choice()
        
        if user_choice == -1:  # Если пользователь выбрал выйти
            print("Спасибо за игру! До свидания!")
            break
        
        computer_choice = get_computer_choice()
        
        choices = ["Камень", "Ножницы", "Бумага"]
        
        print(f"Вы выбрали: {choices[user_choice]}")
        print(f"Компьютер выбрал: {computer_choice}")
        
        result = determine_winner(user_choice, choices.index(computer_choice))
        print(result)
        print()  # Печатаем пустую строку для разделения игр

if __name__ == "__main__":
    play_game()