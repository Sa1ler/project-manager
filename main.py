import func
from modules import calculator, guess, bankomat

while True:
    func.show_menu()
    try:
        number = int(input('Введите номер пункта:'))
    except ValueError:
        print('Ошибка. Введите корректное число.')
        continue

    match number:
        # ===== КАЛЬКУЛЯТОР =====
        case 1:
            calculator.calculator()
        # ===== УГАДАТЬ ЧИСЛО =====
        case 2:
            guess.guess()
        # ===== БАНКОМАТ =====
        case 3:
            bankomat.bankomat()
        case _:
            print('Ошибка. Введите номер пункта от 1 до ')