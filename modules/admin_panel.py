correct_login = "graff"
correct_password = 1234
list = ['Дмитрий', 'Сергей', 'Владимир', 'Александр']
logs = []

def show_menu():
    print('===== Главное меню =====')
    print('1. Список сотрудников') 
    print('2. Кол-во сотрудников')
    print('3. Добавить сотрудника')
    print('4. Удалить сотрудника')
    print('5. Найти сотрудника')
    print('6. Расформировать состав')
    print('7. Логи')
    print('8. Выход')

def input_login():
    print('===== Авторизация =====')
    login = input('Введите ваш логин:')
    password = int(input('Введите ваш пароль:'))
    return login, password

def add(name, list):
    if name in list:
        return False
    list.append(name)
    logs.append(f'Сотрудник {name} принят администратором.')
    return True

def remove(name, list):
    if name not in list:
        return False
    list.remove(name)
    logs.append(f'Сотрудник {name} уволен администратором.')
    return True

def find(name, list):
    return name in list

def clear(list):
    return list.clear()


def admin():
    while True:

        login, password =  input_login()

        if login != correct_login or password != correct_password:
            print('===== Ошибка =====')
            print('Неверный логин или пароль.')
            continue
        else:
            break

    while True:

        show_menu()
        
        try:
            number = int(input('Введите номер пункта: '))
        except ValueError:
            print('===== Ошибка =====')
            print('Введите корректное число.')
            continue

        match number: 
            case 1:
                print('===== Список сотрудников =====')
                if len(list) == 0:
                    print('Список сотрудников пуст.')
                for i, person in enumerate(list, start=1): 
                    print(f'{i}. {person}')

            case 2:
                print('===== Количество сотрудников =====')
                print(f'Количество сотрудников: {len(list)}')

            case 3:
                print('===== Добавление сотрудника =====')
                name = input('Введите имя человека: ')
                if add(name, list):
                    print(f'{name} успешно добавлен.')
                else:
                    print(f'Сотрудник {name} уже есть.')

            case 4:
                print('===== Добавление сотрудника =====')
                name = input('Введите имя сотрудника: ')
                if remove(name, list):
                    print(f'Сотрудник {name} успешно удален.')
                else:
                    print(f'Сотрудника с именем {name} не найдено.')

            case 5:
                print('===== Поиск сотрудника =====')
                name = input('Введите имя сотрудника: ')
                if find(name, list):
                    print('Сотрудник найден.')
                else:
                    print('Сотрудник не найден.')

            case 6:
                print('===== Расформирование компании =====')
                confirmation = input('Вы уверены, что хотите расформировать компанию(да/нет)?: ')
                if confirmation == "да":
                    clear(list)
                    print('Список сотрудников успешно очищен.')
                else:
                    print('Расформирование отменено.')

            case 7:
                print('===== Логирование =====')
                if len(logs) == 0:
                    print('Лог пуст.')
                else:    
                    for i, log in enumerate(logs, start=1):
                        print(f'{i}. {log}')

            case 8:
                print('===== Выход =====')
                print('Вы успешно вышли из программы.')


            case _:
                print('===== Ошибка =====')
                print('Введите номер пункта от 1 до 8.')