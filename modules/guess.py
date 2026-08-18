import random

def generate():
    correct_number = random.randint(1, 50)
    return correct_number

def big_small(user_number):
    if user_number > 50:
        return False
    if user_number < 1:
        return False
    return True

def check_number(user_number, correct_number):
    if user_number > correct_number:
        return "Меньше"
    elif user_number < correct_number:
        return "Больше"

def guess():
    correct_number = generate()
    item = 0
    while True:
        try:
            user_number = int(input('Введите число:'))
        except ValueError:
            print('Ошибка. Введите корректное число.')
            continue
        item += 1

        if not big_small(user_number):
            print('Ошибка. Введите число от 1 до 50.')
        else:
            result = check_number(user_number, correct_number)
            match result:
                case "Больше":
                    print('Загаданное число больше.')
                case "Меньше":
                    print('Загаданное число меньше.')
                case _:
                    print(f'Вы угадали! Загаданное число: {correct_number}. На угадывание у вас ушло {item} попыток.')
                    item = 0
                    confirmation = input('Хотите продолжить(да/нет)?:')
                    if confirmation == "да":
                        correct_number = generate()
                        continue
                    else:
                        break