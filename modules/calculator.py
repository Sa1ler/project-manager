def show_menu():
    print('===== Действие =====')
    print('1. Сложение')
    print('2. Вычитание')
    print('3. Деление')
    print('4. Умножение')
    print('5. Выход')

def input_numbers():
    print('===== Запрос данных =====')
    num1 = float(input('Введите первое число:'))
    num2 = float(input('Введите второе число:'))
    return num1, num2

def add(num1, num2):
    return num1 + num2 

def withdraw(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return False
    return num1 / num2

def calculator():
    while True:
        try:
            num1, num2 = input_numbers()
        except ValueError:
            print('===== Ошибка =====')
            print('Введите корректное число.')
            continue

        show_menu()
        try:
            number = int(input('Введите номер пункта:'))
        except ValueError:
            print('===== Ошибка =====')
            print('Введите корректное число.')
            continue

        match number:
            case 1:
                result = add(num1, num2)
                print('===== Сложение =====')
                print(f'Сумма ваших чисел: {result}')
            case 2:
                result = withdraw(num1, num2)
                print('===== Вычитание =====')
                print(f'Разность ваших чисел: {result}')
            case 3:
                result = divide(num1, num2)
                if not result:
                    print('===== Ошибка =====')
                    print('На 0 делить нельзя.')
                else:
                    print('===== Деление =====')
                    print(f'Частное ваших чисел: {result}')
            case 4:
                result = multiply(num1, num2)
                print('===== Умножение =====')
                print(f'Произведение ваших чисел: {result}')
            case 5:
                print('===== Выход =====')
                print('Вы успешно вышли из программы.')
                break
            case _:
                print('===== Ошибка =====')
                print('Введите число от 1 до 5.')
