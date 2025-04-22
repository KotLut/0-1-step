# ИМПОРТ:
from time import sleep
from random import randint

# ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ:
number_zapusk = 0
game_restart = 1
sec_to_exit = 5
default_levels = 10
player_levels = 10
customize_settings = False
sum_win = 0
sum_game_over = 0
sum_nichya = 0

# ФУНКЦИИ:
def start_window(pusk):
    global number_zapusk, customize_settings
    if customize_settings == True:
        print('НАСТРОЙКИ ПРИМЕНЕНЫ!')
        sleep(1)
        customize_settings = False
    elif number_zapusk < 1:
        print('\tПУСК')
    else:
        print('\tПЕРЕЗАГРУЗКА...')
        print('')
    number_zapusk += 1
    start_win = f'''╔═                ═╗
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║
║▓║█████░░░░░█░░█░▓║
║▓║█░░░█░░░░█░░██░▓║
║▓║█░░░█░░░█░░░░█░▓║
║▓║█░░░█░░█░░░░░█░▓║
║▓║█████░█░░░░░░█░▓║
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║
╚═  \tЗапуск    ═╝
    \t№ {number_zapusk}'''
    for stroka in start_win:
        sleep(0.002)
        print(stroka, end='')
    return '\n'


def first_zapusk(zapusk1):
    print('Игра запущена первый раз!')
    print('Не желаете ли прочесть Справку?')
    print('Нажмите "2" для вызова Справки')
    return ''


def global_exit(gl_exit):
    global game_restart
    global sec_to_exit
    game_restart = 0
    print('')
    print('\tИНИЦИАЛИЗИРОВАН')
    print('\tВЫХОД ИЗ ПРОГРАММЫ!')
    print('ПРОГРАММА ЗАКРОЕТСЯ ЧЕРЕЗ:')
    for sec in range(sec_to_exit,0,-1):
        if sec == 1:
            print(f'\t\t{sec} секунда')
        elif 1 < sec <= 3:
            print(f'\t\t{sec} секунды')
        else:
            print(f'\t\t{sec} секунд')
        sleep(1)
    return ''


def spravka(help):
    print('\t-=СПРАВКА=-')
    print('Отложил интеграцию справки на последующие обновления.')
    print('Пока игра не слишком сложна, потому, просьба, читать сообщения игры')
    print('Да...')
    choose = input('А пока нажми что-нибудь >> ')
    return ''


def edit_level(lvl):
    global default_levels, player_levels, customize_settings
    print('\t(01) Выбор количества уровней')
    if default_levels == player_levels:
        print(f'Уровней по умолчанию: {default_levels}')
    else:
        print(f'Уровней выбрано ранее: {player_levels}')
    while True:
        print('Выберите желаемое количество уровней:', end='')
        pl_levels = input()
        try:
            if type(int(pl_levels)) == int:
                player_levels = int(pl_levels)
                customize_settings = True
                print(f' ПРИНЯТО, теперь уровней: {player_levels}')
            break
        except:
            print('')
            print('\tВВЕДЕННО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!')
            print('')
    return ''


def edit_exit(sec):
    global sec_to_exit, customize_settings
    print('\t(02) Изменение времени выхода')
    while True:
        print('Выберите время (в секундах) для отключения/перезапуска программы >> ', end='')
        sec_ex = input()
        try:
            if type(float(sec_ex)) == float:
                sec_to_exit = int(sec_ex)
                customize_settings = True
                print(f' ПРИНЯТО, теперь время выключения/перезагрузки составит: {player_levels} сек.')
            break
        except:
            print('')
            print('\tВВЕДЕННО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!')
            print('')
    return ''


def settings(setting):
    global default_levels, player_levels, sec_to_exit
    print('\t-=НАСТРОЙКИ=-')
    print('Возможные действия:')
    print('\t╞>"1" - Выбор количества уровней')
    print('\t╘>"2" - Изменение времени выхода')
    print('*Все остальные команды вызывают перезапуск')
    print('')
    choose = input('\t>>')
    if choose == '1':
        print(edit_level(True))
    elif choose == '2':
        print(edit_exit(True))
    return ''


def about_credits(credits):
    print('Здравствуй игрок, если ты видишь это сообщение, значит ты не случайно сюда зашёл.')
    print('Благодарю тебя за выбор и запуск игры, в частности именно "Об авторе".')
    print('Это то самое окошко в котором я могу в одностороннем порядке пожелать тебе удачной игры.')
    return ''


def classic_game(main_game):
    global default_levels, player_levels
    global sum_win, sum_game_over, sum_nichya
    global sec_to_exit

    print('---= Классическая игра =---')
    print('Количество уровней', end='')
    if default_levels == player_levels:
        print(f'(установлено по умолчанию):{default_levels}')
    else:
        print(f'в соответствии с пользовательской настройкой:{player_levels}')
    print('')
    print('ПОЕХАЛИ!')
    print('')

    vern = 0
    nevern = 0
    if default_levels == player_levels:
        lvl = default_levels
    else:
        lvl = player_levels
    for level in range(1,lvl+1):
        print(f'╔═══\t-=УРОВЕНЬ {level}=-\t═══╗')
        shoose = input('Ваше число >>\t')
        randomize = str(randint(0, 1))
        print(f'Рандом = \t{randomize}')
        print('Число выбрано', end=' ')
        if choose == randomize:
            print('ВЕРНО!\t√')
            vern += 1
        else:
            print('НЕВЕРНО.\tX')
            nevern += 1
        print(f'╚═══\t-=УРОВЕНЬ {level}=-\t═══╝')
        sleep(0.01)
        print('')
        print('')

    print('-=ИТОГИ ИГРЫ=-')
    print(f'ПОБЕД: {vern}')
    print(f'ПОРАЖЕНИЙ: {nevern}')
    print('ПОТОМУ', end=' --> ')
    if vern == nevern:
        print("НИЧЬЯ")
        print('\t:|')
        sum_nichya += 1
    elif vern > nevern:
        print('ПОБЕДА!')
        print('\t:)')
        sum_win += 1
    else:
        print('ПОРАЖЕНИЕ')
        print('\t:(')
        sum_game_over += 1

    sleep(1)
    print('ПЕРЕЗАПУСК ЧЕРЕЗ:')
    for sec in range(sec_to_exit, 0, -1):
        if sec == 1:
            print(f'\t\t{sec} секунда')
        elif 1 < sec <= 3:
            print(f'\t\t{sec} секунды')
        else:
            print(f'\t\t{sec} секунд')
        sleep(1)
    return ''


# ОСНОВА
while game_restart:
    print(start_window(True))
    print('---= ДОБРО ПОЖАЛОВАТЬ! =---')
    if number_zapusk == 1:
        print(first_zapusk(True))
    else:
        print('',end='')
    print('---= ГЛАВНОЕ МЕНЮ: =---')
    print('Возможные действия:')
    print('\t╠>"1" - Классическая игра')
    print('\t╠>"2" - Справка')
    print('\t╠>"3" - Настройки')
    print('\t╠>"4" - Статистика')
    print('\t╠═>"5" - Об авторе')
    print('\t╚>"0" - Выход')
    print('*Все остальные команды вызывают перезапуск игры')
    print('')
    choose = input('>>')
    if choose == '1':
        print(classic_game(True))
    elif choose == '2':
        print(spravka(True))
    elif choose == '3':
        print(settings(True))
    elif choose == '4':
        print(about_credits(True))
    elif choose == '0':
        print(global_exit(True))
        break
    else:
        continue

