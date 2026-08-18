import func
from modules import calculator, guess, bankomat, ships

while True:
    func.show_menu()
    try:
        number = int(input('Введите номер пункта:'))
    except ValueError:
        print('===== Ошибка =====')
        print('Введите корректное число.')
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
        # ===== КОРАБЛИ =====
        case 4:
            ships.ships()
        case _:
            print('===== Ошибка =====')
            print('Введите номер пункта от 1 до ')
