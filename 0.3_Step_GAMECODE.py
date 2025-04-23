# ИМПОРТ:
from time import sleep
from random import randint

# ИМПОРТ ГРАФИКИ
try:
    from graphicsASCII import *
except:
    print('ГРАФИКА ИГРЫ НЕ ЗАГРУЖЕНА!')
    print('Посьба подтянуть файл "graphicsASCII"')
    print('в папку с этим файлом')
    print('и перезапустить игру!')
    print('ОКНО ИГРЫ ЗАКРОЕТСЯ ЧЕРЕЗ 5 СЕКУНД.')
    sleep(5)


# ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ:
number_zapusk = 0
game_restart = 1
sec_to_exit = 3
number_intro = 3
default_levels = 10
player_levels = 10
customize_settings = False
sum_win = 0
sum_game_over = 0
sum_nichya = 0

# ФУНКЦИИ:
def start_window(pusk):
    global number_zapusk, customize_settings, number_intro
    if customize_settings == True:
        print('НАСТРОЙКИ ПРИМЕНЕНЫ!')
        sleep(1)
        customize_settings = False
    elif number_zapusk < 1:
        print('\tЗАПУСК ИГРЫ')
    else:
        print('\tПЕРЕЗАГРУЗКА...')
        print('')
    number_zapusk += 1
    # ОКНО ГРАФИКИ1
    if number_intro == 1:
        print(old_start_win(True))
    elif number_intro == 2:
        print(big_start_win(True))
    else:
        print(new_start_win(True))
    print('\tЗАПУСК')
    print(f'\t№ {number_zapusk}')

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
    for seconds in range(sec_to_exit, 0, -1):
        if seconds == 1:
            print(f'\t\t{seconds} секунда')
        elif 1 < seconds <= 3:
            print(f'\t\t{seconds} секунды')
        else:
            print(f'\t\t{seconds} секунд')
        sleep(1)
    return ''


def spravka(game_help):
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


def edit_exit(seconds):
    global sec_to_exit, customize_settings
    print('\t(02) Изменение времени выхода')
    print(f'Сейчас, время выхода составляет: {sec_to_exit}')
    while True:
        print('Выберите время (в секундах) для отключения/перезапуска программы >> ', end='')
        sec_ex = input()
        try:
            if type(float(sec_ex)) == float:
                sec_to_exit = int(sec_ex)
                customize_settings = True
                print(f' ПРИНЯТО, теперь время выключения/перезагрузки составит: {sec_to_exit} сек.')
            break
        except:
            print('')
            print('\tВВЕДЕННО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!')
            print('')
    return ''


def edit_zastavka(seconds):
    global number_intro, customize_settings
    print('\t(03) Выбор варианта заставки игры.')
    while True:
        print('\t╞>"1" - Альфа-версия заставки')
        print('\t╞>"2" - Большая заставка')
        print('\t╘>"3" - Новая заставка (рекомендуется)')
        print('Выберите вариант желаемой заставки >> ', end='')
        zast = input()
        try:
            if type(int(zast)) == int:
                number_intro = int(zast)
                customize_settings = True
                print(f' ПРИНЯТО, выбрана заставка номер: {number_intro}.')
            break
        except:
            print('')
            print('\tВВЕДЕННО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!')
            print('')
    return ''


def settings(setting):
    global default_levels, player_levels, sec_to_exit, edit_zastavka
    print('\t-=НАСТРОЙКИ=-')
    print('Возможные действия:')
    print('\t╞>"1" - Выбор количества уровней')
    print('\t╞>"2" - Изменение времени выхода')
    print('\t╘>"3" - Выбор варианта заставки')
    print('*Все остальные команды вызывают перезапуск')
    print('')
    choose = input('\t>>')
    if choose == '1':
        print(edit_level(True))
    elif choose == '2':
        print(edit_exit(True))
    elif choose == '3':
        print(edit_zastavka(True))
    return ''


def about_credits(credits):
    print('\t-=От автора=-')
    print('Здравствуй игрок, если ты видишь это сообщение, значит ты не случайно сюда зашёл.')
    print('Благодарю тебя за выбор и запуск игры, в частности именно "От автора".')
    print('Это то самое окошко в котором я могу в одностороннем порядке пожелать тебе удачной игры.')
    print('')
    print('\t(PS: попробуй ввести "10" в главном меню ;)')
    choose = input('\t>>')
    if choose == '10':
        print('Да не здесь! (^-^")')
        sleep(2)
    return ''


def stats(statistics):
    global sum_win, sum_nichya, sum_game_over, number_zapusk
    print('\t-=Статистика=-')
    print(f'\t\t╟ПОБЕД:{sum_win}')
    print(f'\t\t╟ВНИЧЬЮ:{sum_nichya}')
    print(f'\t\t╟ПОРАЖЕНИЙ:{sum_game_over}')
    print(f'\t\t╙ЗАПУСКОВ ПРОГРАММЫ:{number_zapusk}')
    print('')
    choose = input('Введите что-либо чтобы продолжить >> ')
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
    print('\t╠═>"5" - От автора')
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
        print(stats(True))
    elif choose == '5':
        print(about_credits(True))
    elif choose == '0':
        print(global_exit(True))
        break
    elif choose == '10':
        print(logo_author(True))
    else:
        continue
