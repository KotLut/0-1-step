# ИМПОРТ:
from time import sleep
from random import randint
from os import name, system


# ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ:
number_zapusk = 0
game_restart = True
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
ochist = True


# КЛАСС АЧИВОК
class Achieve:
    customize_set = 0
    old_win = 0
    big_win = 0
    ochistka = True
    ochistka2 = False
    creditss = False
    logo = False
    ten = False
    hello_world = False



# ИМПОРТ ГРАФИКИ
try:
    from graphicsASCII import *
except ModuleNotFoundError:
    print('''\tГРАФИКА ИГРЫ НЕ ЗАГРУЖЕНА!
    \tВозможно вы запускаете игру из Архива,
    \tтогда разархивируйте папку. Иначе
    \tпросьба подтянуть файл "graphicsASCII"
    \tв папку с этим файлом
    \tи перезапустить игру!

    \tОКНО ИГРЫ ЗАКРОЕТСЯ ЧЕРЕЗ 5 СЕКУНД.''')
    sleep(5)
    game_restart = False


# ФУНКЦИИ:
def start_window():
    global number_zapusk, customize_settings, number_intro
    if customize_settings:
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
        print(old_start_win())
        Achieve.old_win += 1
    elif number_intro == 2:
        print(big_start_win())
        Achieve.big_win += 1
    else:
        print(new_start_win())
    print('\tЗАПУСК')
    print(f'\t№ {number_zapusk}')

    return '\n'


def necor_zn():
    return '\n\tВВЕДЕННО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!\n'

def waiting():
    return input('Введите что-нибудь, чтобы продолжить >> ')


def screen_clear():
    if ochist:
        if name == 'nt': # Windows
            system('cls')
        elif name == 'posix':    # Unix (Linux or macOS)
            system('clear')


def first_zapusk():
    print('Игра запущена первый раз!')
    print('Не желаете ли прочесть Справку?')
    print('Нажмите "5" для вызова Справки')
    return ''


def global_exit():
    screen_clear()
    global game_restart, sec_to_exit
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


def spravka():
    screen_clear()
    print('\t-=СПРАВКА=-')
    print('Отложил интеграцию справки на последующие обновления.')
    print('Пока игра не слишком сложна, потому, просьба, читать сообщения игры')
    print('Да...')
    input('А пока нажми что-нибудь >> ')
    return ''


def edit_level():
    screen_clear()
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
                Achieve.customize_set += 1
                print(f'ПРИНЯТО, теперь уровней: {player_levels}')
                waiting()
            break
        except ValueError:
            print(necor_zn())
    return settings()


def edit_podskazka():
    screen_clear()
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
                    print(necor_zn())
                else:
                    player_podskaz = int(pl_podsk)
                    customize_settings = True
                    Achieve.customize_set += 1
                    print(f'ПРИНЯТО, теперь частота подсказок = {player_podskaz}')
                    break
        except ValueError:
            print(necor_zn())
    return settings()


def edit_xp():
    screen_clear()
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
        pl_xp = input()
        try:
            if type(int(pl_xp)) == int:
                if int(pl_xp) == 0:
                    print(necor_zn())
                else:
                    player_XP = int(pl_xp)
                    customize_settings = True
                    Achieve.customize_set += 1
                    print(f'ПРИНЯТО, теперь здоровья: {player_podskaz}')
                    break
        except ValueError:
            print(necor_zn())
    return settings()



def edit_exit():
    screen_clear()
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
                Achieve.customize_set += 1
                print(f'ПРИНЯТО, теперь время выключения/перезагрузки составит: {sec_to_exit} сек.')
            break
        except ValueError:
            print(necor_zn())
    return settings()


def edit_zastavka():
    screen_clear()
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
                Achieve.customize_set += 1
                print(f'ПРИНЯТО, выбрана заставка номер: {number_intro}.')
            break
        except ValueError:
            print(necor_zn())
    return settings()


def settings():
    global ochist
    screen_clear()
    print('')
    print('\t-=НАСТРОЙКИ=-')
    print('Возможные действия:')
    print('\t╞>"1" - Выбор количества уровней')
    print('\t╞>"2" - Выбор количества подсказок')
    print('\t╞>"3" - Выбор количества здоровья')
    print('\t╞>"4" - Изменение времени выхода')
    print('\t╞>"5" - Выбор варианта заставки')
    print('\t╘>"0" - Вкл./Выкл. Обновления экрана')
    print('*Все остальные команды вызывают перезапуск')
    print('')
    settings_choose = input('\t>>')
    if settings_choose == '1':
        print(edit_level())
    elif settings_choose == '2':
        print(edit_podskazka())
    elif settings_choose == '3':
        print(edit_xp())
    elif settings_choose == '4':
        print(edit_exit())
    elif settings_choose == '5':
        print(edit_zastavka())
    elif settings_choose == '0':
        if ochist:
            ochist = False
            print('\tВЫКЛючено обновление экрана')
            Achieve.ochistka = False
        else:
            ochist = True
            print('\tВКЛючено обновление экрана')
            if not Achieve.ochistka:
                Achieve.ochistka2 = True
        waiting()
    return ''


def about_credits():
    screen_clear()
    print('\t-=От автора=-')
    print('Здравствуй игрок, если ты видишь это сообщение, значит ты не случайно сюда зашёл.')
    print('Благодарю тебя за выбор и запуск игры, в частности именно "От автора".')
    print('Это то самое окошко в котором я могу в одностороннем порядке пожелать тебе удачной игры.')
    print('')
    print('\t(PS: попробуй ввести "10" в главном меню ;)')
    credits_choose = input('\t>>')
    if credits_choose == '10':
        print('Да не здесь! (^-^")')
        sleep(2)
        Achieve.ten = True
    Achieve.creditss = True
    return ''


def dostyagi():
    screen_clear()
    global number_zapusk, sum_win, sum_nichya, sum_game_over
    print('\t---=ДОСТИЖЕНИЯ=---')
    print('')
    print('\tКЛАССИЧЕСКИЕ:')
    if number_zapusk > 0:
        print(f'\t╠═> ЗАПУСК_01: Перезапустить "01_Step" 10 и более раз')
    else:
        print('\t╟')
    if number_zapusk >= 30 :
        print(f'\t╠═> ЗАПУСК_30: Перезапустить "01_Step" 30 и более раз')
    else:
        print('\t╟')
    if number_zapusk >= 50:
        print(f'\t╠═> ЗАПУСК_50+: Перезапустить "01_Step" 50 и более раз ({number_zapusk})')
        print('\t║               (За дальнейшие перезапуски достижения не предусмотрено!)')
    else:
        print('\t╟')

    if sum_win >= 3:
        print(f'\t╠═> МОЛОДЕЦ: Выиграть 3 и более раз')
    else:
        print('\t╟')
    if sum_win >= 10:
        print(f'\t╠═> ХОРОШ: Выиграть 10 и более раз')
    else:
        print('\t╟')
    if sum_win >= 15:
        print(f'\t╠═> КРАСАВЧИК: Выиграть 15 и более раз ({sum_win})')
        print('\t║               (За дальнейшие выигрыши достижения не предусмотрено!)')
    else:
        print('\t╟')

    if sum_nichya > 0:
        print(f'\t╠═> ВОУ!: Хотя бы раз сыграть ВНИЧЬЮ ({sum_nichya})')
    else:
        print('\t╟')

    if sum_game_over >= 3:
        print(f'\t╠═> БЫВАЕТ: Проиграть 3 и более раз ({sum_game_over})')
    else:
        print('\t╟')
    if sum_game_over >= 10:
        print(f'\t╚═> ЭХЪ: Выиграть 10 и более раз ({sum_win})')
        print('\t                (За дальнейшие проигрыши достижения не предусмотрено!)')
    else:
        print('\t╙')
    print('\t')

    print('\tНЕСТАНДАРТНЫЕ:')
    if Achieve.customize_set >= 5:
        print(f'\t╠═> МЕНЯТОР: Изменить настройки игры 5 и более раз ({Achieve.customize_set })')
    else:
        print('\t╟')
    if Achieve.old_win > 0:
        print(f'\t╠═> ALPHA-LOGO: Увидеть Альфа-версию заставки ({Achieve.old_win})')
    else:
        print('\t╟')
    if Achieve.big_win > 0:
        print(f'\t╠═> BIG-LOGO: Увидеть большую версию заставки ({Achieve.big_win})')
    else:
        print('\t╟')
    if not Achieve.ochistka:
        print(f'\t╠═> ЛИНИЯМИ: Убрать автоочистку aka. ВЫКЛючить автообновление экрана')
    else:
        print('\t╟')
    if Achieve.ochistka2:
        print(f'\t╠═> ТАК_ЛУЧШЕ: Всё-таки включить автооичтску aka. снова ВКЛючить автообновление экрана')
    else:
        print('\t╟')
    if Achieve.creditss:
        print(f'\t╚═> ЧИТАТЕЛЬ: Посмотреть раздел "От автора"')
    else:
        print('\t╙')
    print('\t')

    print('\tРЕДКИЕ:')
    if Achieve.ten:
        print(f'\t╠═> ^-^: Увидеть микро-пасхалку в разделе "От автора" ({Achieve.customize_set })')
    else:
        print('\t╟')
    if Achieve.logo:
        print(f'\t╚═> ВПЕЧАТЛЁН?: "Выбрать" пасхалку "10" в Главном меню')
    else:
        print('\t╙')
    print('')
    print('\tКОДЕРОВСКАЯ:\n\t(OPEN-SOURCE code)')
    if Achieve.hello_world:
        print(f'\t╚═> МЕГАХОРОШ: Поменять параметр в окончании файла игры')
    else:
        print('\t╙X','Найди "hello_world" в коде. Пофикси ;)')
    print('')
    waiting()
    return ''


def stats():
    screen_clear()
    global sum_win, sum_nichya, sum_game_over, number_zapusk
    print('\t---=СТАТИСТИКА=---')
    print(f'\t\t╟ПОБЕД:{sum_win}')
    print(f'\t\t╟ВНИЧЬЮ:{sum_nichya}')
    print(f'\t\t╟ПОРАЖЕНИЙ:{sum_game_over}')
    print(f'\t\t╙ЗАПУСКОВ ПРОГРАММЫ:{number_zapusk}')
    print('')
    waiting()
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


def classic_game():
    screen_clear()
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
        choice_choose = input('║Ваше число >>\t')
        randomize = str(randint(0, 1))
        print(f'║Рандом = \t{randomize}')
        if choice_choose == randomize:
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
    waiting()


def all_or_nothing():
    screen_clear()
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
    waiting()


def podskaz_game():
    screen_clear()
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
            podskaz_choose = input('║Ваше число !!\t')

        else:
            print(f'╔═══\t-= УРОВЕНЬ {level} =-\t═══╗')
            podskaz_choose = input('║Ваше число >>\t')
            randomize = str(randint(0, 1))
            print(f'║Рандом = \t{randomize}')

        if podskaz_choose == randomize:
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
    waiting()


def xp_game():
    screen_clear()
    global default_XP, player_XP

    print('---= Режим игры "ЖИЗНИ" =---')
    print('Количество здоровья', end='')
    if default_XP == player_XP:
        print(f'(установлено по умолчанию):')
        print(f'\t{default_XP}', '♥'*default_XP)
        xp = default_XP
    else:
        print(f'(в соответствии с пользовательской настройкой):')
        print(f'\t{player_XP}', '♥'*player_XP)
        xp = player_XP
    print('')
    print('ПОЕХАЛИ!')
    print('')

    vern = 0
    nevern = 0
    level = 0
    while xp > 0:
        level += 1
        print('\t',f'{xp}','♥'*xp)
        print(f'╔═══\t-= УРОВЕНЬ {level} =-\t═══╗')
        xp_choose = input('║Ваше число >>\t')
        randomize = str(randint(0, 1))
        print(f'║Рандом = \t{randomize}')
        if xp_choose == randomize:
            print('║ВЕРНО!\t\t√  ')
            vern += 1
        else:
            print('║НЕВЕРНО.\tX  ')
            nevern += 1
            xp -= 1
        print(f'╚═══\t-= Здоровья: {xp}♥ =-\t═══╝')
        sleep(0.01)
        print('')
        print('')
    sleep(0.5)
    print(itogi_game(vern, nevern))
    waiting()



# ОСНОВА
base = 'teleport'
while game_restart:
    screen_clear()
    print(start_window())
    print('---= ДОБРО ПОЖАЛОВАТЬ! =---')
    if number_zapusk == 1:
        print(first_zapusk())
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
    print('\t╠>"8" - Достижения')
    print('\t╠═>"9" - "От автора"')
    print('\t╚>"0" - Выход')
    print('* Все остальные команды вызывают перезапуск игры',end='')
    if not Achieve.logo:
        print('')
    else:
        print('**\t\t**Почти все ;)')
    choose = input('>>')
    if choose == '1':
        print(classic_game())
    elif choose == '2':
        print(all_or_nothing())
    elif choose == '3':
        print(xp_game())
    elif choose == '4':
        print(podskaz_game())
    elif choose == '5':
        print(spravka())
    elif choose == '6':
        print(settings())
    elif choose == '7':
        print(stats())
    elif choose == '8':
        print(dostyagi())
    elif choose == '9':
        print(about_credits())
    elif choose == '0':
        print(global_exit())
        break
    elif choose == '10':
        print(logo_author())
        Achieve.logo = True
    else:
        continue
Achieve.hello_world = False
