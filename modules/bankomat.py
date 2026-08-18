def show_menu():
    print('1. Баланс')
    print('2. Пополнить баланс')
    print('3. Списать средства')
    print('4. Проверить PIN')
    print('5. История')
    print('6. Выход')

def add(balance, sum):
    return balance + sum

def withdraw(balance, sum):
    return balance - sum

def check_pin(user_pin, correct_pin):
    return correct_pin == correct_pin

def bankomat():
    balance = 5000
    PinCode = 1234
    history = []
    while True:
        show_menu()
        try:
            number = int(input('Введите номер пункта:'))
        except ValueError:
            print('Ошибка. Введите корректное число.')
            continue
        match number:
            case 1:
                print(f'Ваш баланс: {balance}')
            case 2:
                try:
                    add_sum = float(input('Введите сумму пополнения:'))
                except ValueError:
                    print('Ошибка. Введите корректную сумму:')
                    continue
                if add_sum < 1:
                    print('Ошибка. Введите положительную сумму пополнения.')
                else:
                    balance = add(balance, add_sum)
                    history.append(f"Пополнение на сумму {add_sum}.")
                    print(f'Баланс успшно пополнен на сумму {add_sum}.\nТекущий баланс: {balance}')
            case 3:
                try:
                    withdraw_sum = float(input('Введите сумму для списания:'))
                except ValueError:
                    print('Ошибка. Введите корректную сумму пополнения.')
                if withdraw_sum < 1 or withdraw_sum > balance:
                    print('Ошибка. Введите корректное число непривышающее ваш баланс.')
                else:
                    balance = withdraw(balance, withdraw_sum)
                    history.append(f"Списание на сумму {withdraw_sum}.")
                    print(f'Успешно списано {withdraw_sum} с вашего счета.\nТекущий баланс: {balance}')
            case 4:
                try:
                    user_pin = int(input('Введите ваш PinCode для проверки:'))
                except ValueError:
                    print('Ошибка. Введите корректный PinCode.')
                    continue
                if check_pin(user_pin, PinCode):
                    print('PinCode верен.')
                else:
                    print('PinCode неверен.')
            case 5:
                for i, item in enumerate(history, start=1):
                    print(f'{i}. {item}')
            case 6:
                print('Программа успешно закрыта.')
                break