def input_health():
    user_health = int(input('Введите кол-во здоровья своего корабля: '))
    opponent_health = int(input('Введите кол-во здоровья вражеского корабля: '))
    return user_health, opponent_health

def input_damage():
    user_damage = int(input('Введите кол-во урона у вашего корабля за 1 выстрел: '))
    opponent_damage = int(input('Введите кол-во урона у вражеского корабля за 1 выстрел: '))
    return user_damage, opponent_damage

def input_count():
    user_count = int(input('Введите кол-во выстрелов у вашего корабля за раз: '))
    opponent_count = int(input('Введите кол-во выстрелов у вражеского корабля за раз: '))
    return user_count, opponent_count

def damage(user_damage, user_count, opponent_damage, opponent_count):
    all_user_damage = user_damage * user_count
    all_opponent_damage = opponent_damage * opponent_count
    return all_user_damage, all_opponent_damage

def results(all_user_damage, all_opponent_damage, user_health, opponent_health):
    user_result = all_opponent_damage / opponent_health
    opponent_result = all_opponent_damage / user_health
    return user_result, opponent_result

def check_winner(user_result, opponent_result):
    if user_result < opponent_result:
        return 'Победа'
    elif user_result > opponent_result:
        return 'Поражение'

def ships():
    while True:
        try:
            user_health, opponent_health = input_health()
            user_damage, opponent_damage = input_damage()
            user_count, opponent_count = input_count()
        except ValueError:
            print('===== Ошибка =====')
            print('Введите корректные значения.')
            continue
        
        all_user_damage, all_opponent_damage = damage(user_damage, user_count, opponent_damage, opponent_count)
        user_result, opponent_result = results(all_user_damage, all_opponent_damage, user_health, opponent_health)
        
        winner = check_winner(user_result, opponent_result)

        print('===== Результат =====')

        if winner == 'Победа':
            print('Вы выиграли!')
        elif winner == 'Поражение':
            print('Вы проиграли:(')
        else:
            print('Ничья.')
