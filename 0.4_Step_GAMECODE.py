# ИМПОРТ:
from time import sleep
from random import randint

# ИМПОРТ ГРАФИКИ
try:
    from graphicsASCII import *
except:
    print('''\tГРАФИКА ИГРЫ НЕ ЗАГРУЖЕНА!
    \tВозможно вы запускаете игру из Архива,
    \tтогда разархивируйте папку. Иначе
    \tпросьба подтянуть файл "graphicsASCII"
    \tв папку с этим файлом
    \tи перезапустить игру!
    
    \tОКНО ИГРЫ ЗАКРОЕТСЯ ЧЕРЕЗ 5 СЕКУНД.''')
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
default_podskaz = 4
player_podskaz = 4
default_XP = 5
player_XP = 5

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
    print('Нажмите "5" для вызова Справки')
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
                print(f'ПРИНЯТО, теперь уровней: {player_levels}')
            break
        except:
            print('')
            print('\tВВЕДЕННО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!')
            print('')
    return settings(True)


def edit_podskazka(podsk):
    global default_podskaz, player_podskaz, customize_settings
    print('\t(02) Выбор количества подсказок')
    print('Через какое кол-во уровней будут появляться подсказки')
    print('в режиме игры с подсказками.')
    print('1 - означает частоту в каждый уровень. Чем больше значение,')
    print('тем реже будет появляться подсказка.')
    if default_podskaz == player_podskaz:
        print(f'Частота подсказок по умолчанию: {default_podskaz}')
    else:
        print(f'Частота подсказок, выбранная ранее: {player_podskaz}')
    while True:
        print('Выберите частоту подсказок на уровнях:', end='')
        pl_podsk = input()
        try:
            if type(int(pl_podsk)) == int:
                if int(pl_podsk) == 0:
                    print('НЕККОРЕКТНОЕ ЗНАЧЕНИЕ!')
                else:
                    player_podskaz = int(pl_podsk)
                    customize_settings = True
                    print(f'ПРИНЯТО, теперь частота подсказок = {player_podskaz}')
                    break
        except:
            print('')
            print('\tВВЕДЕННО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!')
            print('')
    return settings(True)


def edit_XP(zdorov):
    global default_XP, player_XP, customize_settings
    print('\t(03) Выбор количества здоровья')
    print('От здоровья зависит длительность режима игры "ЖИЗНИ".')
    print('Чем больше значение - тем дольше будет длиться игра.')
    if default_XP == player_XP:
        print(f'Количество здоровья по умолчанию: {default_XP}')
    else:
        print(f'Количество здоровья, выбранное ранее: {player_XP}')
    while True:
        print('Выберите количество здоровья на уровнях:', end='')
        pl_XP = input()
        try:
            if type(int(pl_XP)) == int:
                if int(pl_XP) == 0:
                    print('НЕККОРЕКТНОЕ ЗНАЧЕНИЕ!')
                else:
                    player_XP = int(pl_XP)
                    customize_settings = True
                    print(f'ПРИНЯТО, теперь здоровья: {player_podskaz}')
                    break
        except:
            print('')
            print('\tВВЕДЕННО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!')
            print('')
    return settings(True)



def edit_exit(seconds):
    global sec_to_exit, customize_settings
    print('\t(04) Изменение времени выхода')
    print(f'Сейчас, время выхода составляет: {sec_to_exit}')
    while True:
        print('Выберите время (в секундах) для отключения/перезапуска программы >> ', end='')
        sec_ex = input()
        try:
            if type(float(sec_ex)) == float:
                sec_to_exit = int(sec_ex)
                customize_settings = True
                print(f'ПРИНЯТО, теперь время выключения/перезагрузки составит: {sec_to_exit} сек.')
            break
        except:
            print('')
            print('\tВВЕДЕННО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!')
            print('')
    return settings(True)


def edit_zastavka(seconds):
    global number_intro, customize_settings
    print('\t(05) Выбор варианта заставки игры.')
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
                print(f'ПРИНЯТО, выбрана заставка номер: {number_intro}.')
            break
        except:
            print('')
            print('\tВВЕДЕННО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!')
            print('')
    return settings(True)


def settings(setting):
    print('')
    print('\t-=НАСТРОЙКИ=-')
    print('Возможные действия:')
    print('\t╞>"1" - Выбор количества уровней')
    print('\t╞>"2" - Выбор количества подсказок')
    print('\t╞>"3" - Выбор количества здоровья')
    print('\t╞>"4" - Изменение времени выхода')
    print('\t╘>"5" - Выбор варианта заставки')
    print('*Все остальные команды вызывают перезапуск')
    print('')
    choose = input('\t>>')
    if choose == '1':
        print(edit_level(True))
    elif choose == '2':
        print(edit_podskazka(True))
    elif choose == '3':
        print(edit_XP(True))
    elif choose == '4':
        print(edit_exit(True))
    elif choose == '5':
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


def itogi_game(vern,nevern):
    global sum_win, sum_game_over, sum_nichya
    print('\t\t-=ИТОГИ ИГРЫ=-')
    print(f'\tПОБЕД: {vern}')
    print(f'\tПОРАЖЕНИЙ: {nevern}')
    print('\tПОТОМУ', end=' --> ')
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
    return ''


def classic_game(main_game):
    global default_levels, player_levels

    print('---= Классическая игра =---')
    print('Количество уровней', end='')
    if default_levels == player_levels:
        print(f'(установлено по умолчанию):{default_levels}')
        lvl = default_levels
    else:
        print(f'в соответствии с пользовательской настройкой:{player_levels}')
        lvl = player_levels
    print('')
    print('ПОЕХАЛИ!')
    print('')

    vern = 0
    nevern = 0
    for level in range(1,lvl+1):
        print(f'╔═══\t-= УРОВЕНЬ {level} =-\t═══╗')
        choose = input('║Ваше число >>\t')
        randomize = str(randint(0, 1))
        print(f'║Рандом = \t{randomize}')
        if choose == randomize:
            print('║ВЕРНО!\t\t√  ')
            vern += 1
        else:
            print('║НЕВЕРНО.\tX  ')
            nevern += 1
        print(f'╚═══\t-= УРОВЕНЬ {level} =-\t═══╝')
        sleep(0.01)
        print('')
        print('')
    sleep(0.5)
    print(itogi_game(vern,nevern))
    input('Введите что-либо, чтобы продолжить >>')


def all_or_nothing(mod1):
    global default_levels, player_levels

    print('---= Режим игры "Всё или ничего" =---')
    print('Количество уровней', end='')
    if default_levels == player_levels:
        print(f'(установлено по умолчанию):{default_levels}')
        lvl = default_levels
    else:
        print(f'в соответствии с пользовательской настройкой:{player_levels}')
        lvl = player_levels

    print('')
    print('ПОЕХАЛИ!')
    print('')
    numer = input('Ваше число >> ')

    vern = 0
    nevern = 0
    print(f'╔════\t\t-= ВСЁ ИЛИ НИЧЕГО =-\t\t════╗')
    print('║\t| Ур.\t| №\t| Сл.Ч.\t|+/-| \t\t    ║')
    for level in range(1, lvl + 1):
        randomize = str(randint(0, 1))
        print(f'║\t| {level}\t| {numer}\t| {randomize}\t|',end=' ')
        if numer == randomize:
            print('√ |\t\t    ║')
            vern += 1
        else:
            print('X |\t\t    ║')
            nevern += 1
        sleep(0.1)
    print(f'╚════\t════════════════════════════════\t════╝')
    print('')
    sleep(1.1)
    print(itogi_game(vern,nevern))
    input('Введите что-либо, чтобы продолжить >>')


def podskaz_game(mod2):
    global default_levels, player_levels
    global default_podskaz, player_podskaz

    print('---= Игра с подсказками! =---')
    print(f'Подсказки будут появляться раз в ', end='')
    if default_podskaz == player_podskaz:
        print(f'(установлено по умолчанию):{default_podskaz} ур.')
        pods = default_podskaz
    else:
        print(f'(в соответствии с пользовательской настройкой):{player_podskaz} ур.')
        pods = player_podskaz
    print('Количество уровней', end='')
    if default_levels == player_levels:
        print(f'(установлено по умолчанию):{default_levels}')
        lvl = default_levels
    else:
        print(f'(в соответствии с пользовательской настройкой):{player_levels}')
        lvl = player_levels
    print('')
    print('ПОЕХАЛИ!')
    print('')

    vern = 0
    nevern = 0

    for level in range(1, lvl + 1):
        if level % pods == 0:
            print(f'╔═══\t-= УРОВЕНЬ {level} =-\t═══╗')
            randomize = str(randint(0, 1))
            print(f'║РАНДОМ = \t{randomize}')
            choose = input('║Ваше число !!\t')

        else:
            print(f'╔═══\t-= УРОВЕНЬ {level} =-\t═══╗')
            choose = input('║Ваше число >>\t')
            randomize = str(randint(0, 1))
            print(f'║Рандом = \t{randomize}')

        if choose == randomize:
            print('║ВЕРНО!\t\t√  ')
            vern += 1
        else:
            print('║НЕВЕРНО.\tX  ')
            nevern += 1
        print(f'╚═══\t-= УРОВЕНЬ {level} =-\t═══╝')
        sleep(0.01)
        print('')
        print('')
    sleep(1.1)
    print(itogi_game(vern,nevern))
    input('Введите что-либо, чтобы продолжить >>')


def XP_game(mod3):
    global default_XP, player_XP

    print('---= Режим игры "ЖИЗНИ" =---')
    print('Количество здоровья', end='')
    if default_XP == player_XP:
        print(f'(установлено по умолчанию):')
        print(f'\t{default_XP}', '♥'*default_XP)
        XP = default_XP
    else:
        print(f'(в соответствии с пользовательской настройкой):')
        print(f'\t{player_XP}', '♥'*player_XP)
        XP = player_XP
    print('')
    print('ПОЕХАЛИ!')
    print('')

    vern = 0
    nevern = 0
    level = 0
    while XP > 0:
        level += 1
        print('\t',f'{XP}','♥'*XP)
        print(f'╔═══\t-= УРОВЕНЬ {level} =-\t═══╗')
        choose = input('║Ваше число >>\t')
        randomize = str(randint(0, 1))
        print(f'║Рандом = \t{randomize}')
        if choose == randomize:
            print('║ВЕРНО!\t\t√  ')
            vern += 1
        else:
            print('║НЕВЕРНО.\tX  ')
            nevern += 1
            XP -= 1
        print(f'╚═══\t-= Здоровья: {XP}♥ =-\t═══╝')
        sleep(0.01)
        print('')
        print('')
    sleep(0.5)
    print(itogi_game(vern, nevern))
    input('Введите что-либо, чтобы продолжить >>')



# ОСНОВА
base = 'teleport'
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
    print('\t╠>"2" - Режим "Всё или ничего"')
    print('\t╠>"3" - Режим "ЖИЗНИ"')
    print('\t╠>"4" - Режим игры с подсказками"')
    print('\t╠>"5" - Справка')
    print('\t╠>"6" - Настройки')
    print('\t╠>"7" - Статистика')
    print('\t╠═>"9" - От автора')
    print('\t╚>"0" - Выход')
    print('*Все остальные команды вызывают перезапуск игры')
    print('')
    choose = input('>>')
    if choose == '1':
        print(classic_game(True))
    elif choose == '2':
        print(all_or_nothing(True))
    elif choose == '3':
        print(XP_game(True))
    elif choose == '4':
        print(podskaz_game(True))
    elif choose == '5':
        print(spravka(True))
    elif choose == '6':
        print(settings(True))
    elif choose == '7':
        print(stats(True))
    elif choose == '9':
        print(about_credits(True))
    elif choose == '0':
        print(global_exit(True))
        break
    elif choose == '10':
        print(logo_author(True))
    else:
        continue
