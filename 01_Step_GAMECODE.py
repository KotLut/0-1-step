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
default_xp = 5
player_xp = 5
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
    graphica = open('graphicsASC.txt', encoding='utf-8', errors='ignore').readlines()
except FileNotFoundError:
    print('''\tГРАФИКА ИГРЫ НЕ ЗАГРУЖЕНА!
    \tВозможно вы запускаете игру из Архива,
    \tтогда разархивируйте папку. Иначе
    \tпросьба подтянуть файл "graphicsASC"
    \tв папку с этим файлом
    \tи перезапустить игру!

    \t"ЭТО ОКНО ЗАКРОЕТСЯ ЧЕРЕЗ 5 СЕКУНД.''')
    graphica = ['// Здесь должна быть графика! //']*170
    sleep(5)


# ФУНКЦИИ:
def graphics(num):
    if num == 1:
        old_s_win = graphica[0:9]
        for wind in old_s_win:
            wind = wind.replace('\n', '')
            sleep(0.002)
            print(wind)
    elif num == 2:
        big_s_win = graphica[11:55]
        for wind in big_s_win:
            wind = wind.replace('\n', '')
            sleep(0.002)
            print(wind)
    elif num == 3:
        new_s_win = graphica[56:87]
        for wind in new_s_win:
            wind = wind.replace('\n', '')
            sleep(0.002)
            print(wind)
    else:
        new_s_win = graphica[88:169]
        print(*new_s_win)


def start_window():
    global number_zapusk, customize_settings, number_intro
    if customize_settings:
        print('| НАСТРОЙКИ ПРИМЕНЕНЫ! |')
        sleep(1)
        customize_settings = False
    elif number_zapusk < 1:
        print('\t| ЗАПУСК ИГРЫ |')
    else:
        print('\t| ПЕРЕЗАГРУЗКА... |')
        print('')
    number_zapusk += 1

    # ОКНО ГРАФИКИ1
    if number_intro == 1:
        graphics(1)
        Achieve.old_win += 1
    elif number_intro == 2:
        graphics(2)
        Achieve.big_win += 1
    else:
        graphics(3)
    print('\t| ЗАПУСК |')
    print(f'\t| № {number_zapusk}\t |')


def necor_zn():
    return '\n\t| ВВЕДЕННО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ! |\n'

def waiting():
    return input('\tВведите что-нибудь, чтобы продолжить >> ')


def screen_clear():
    if ochist:
        if name == 'nt': # Windows
            system('cls')
        elif name == 'posix':    # Unix (Linux or macOS)
            system('clear')


def global_exit():
    screen_clear()
    global game_restart, sec_to_exit
    game_restart = 0
    print('')
    print('\t|    ИНИЦИАЛИЗИРОВАН\t|')
    print('\t|  ВЫХОД ИЗ ПРОГРАММЫ!\t|')
    print('\tПРОГРАММА ЗАКРОЕТСЯ ЧЕРЕЗ:')
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
    print('\n\t\t---/===/  СПРАВКА  \===\---\n')
    print('Отложил интеграцию справки на последующие обновления.')
    print('Пока игра не слишком сложна, потому, просьба, читать сообщения игры')
    print('Да...')
    waiting()
    return ''


def edit_level():
    screen_clear()
    global default_levels, player_levels, customize_settings
    print('\n\t| (01) Выбор количества уровней |\n')
    if default_levels == player_levels:
        print(f'\tУровней по умолчанию: {default_levels}')
    else:
        print(f'\tУровней выбрано ранее: {player_levels}')
    while True:
        print('\tВыберите желаемое количество уровней:', end='')
        pl_levels = input()
        try:
            if type(int(pl_levels)) == int:
                player_levels = int(pl_levels)
                customize_settings = True
                Achieve.customize_set += 1
                print(f'\n\tПРИНЯТО, теперь уровней: {player_levels}\n')
                waiting()
            break
        except ValueError:
            print(necor_zn())
    return settings()


def edit_podskazka():
    screen_clear()
    global default_podskaz, player_podskaz, customize_settings
    print('\n\t| (02) Выбор количества подсказок |\n')
    print('\t//Через какое кол-во уровней будут появляться подсказки')
    print('\t\\\в режиме игры с подсказками.')
    print('\t//"1" - означает частоту в каждый уровень. Чем больше,')
    print('\t\\\значение, тем реже будет появляться подсказка.\n')
    if default_podskaz == player_podskaz:
        print(f'\tЧастота подсказок по умолчанию: {default_podskaz}')
    else:
        print(f'\tЧастота подсказок, выбранная ранее: {player_podskaz}')
    while True:
        print('\tВыберите частоту подсказок на уровнях:', end='')
        pl_podsk = input()
        try:
            if type(int(pl_podsk)) == int:
                if int(pl_podsk) == 0:
                    print(necor_zn())
                else:
                    player_podskaz = int(pl_podsk)
                    customize_settings = True
                    Achieve.customize_set += 1
                    print(f'\n\tПРИНЯТО, теперь частота подсказок = {player_podskaz}\n')
                    waiting()
                    break
        except ValueError:
            print(necor_zn())
    return settings()


def edit_xp():
    screen_clear()
    global default_xp, player_xp, customize_settings
    print('\n\t| (03) Выбор количества здоровья |\n')
    print('\t//От здоровья зависит длительность режима игры "ЖИЗНИ".')
    print('\t\\\Чем больше значение - тем дольше будет длиться игра.\n')
    if default_xp == player_xp:
        print(f'\tКоличество здоровья по умолчанию: {default_xp}')
    else:
        print(f'\tКоличество здоровья, выбранное ранее: {player_xp}')
    while True:
        print('\tВыберите количество здоровья на уровнях:', end='')
        pl_xp = input()
        try:
            if type(int(pl_xp)) == int:
                if int(pl_xp) == 0:
                    print(necor_zn())
                else:
                    player_xp = int(pl_xp)
                    customize_settings = True
                    Achieve.customize_set += 1
                    print(f'\n\tПРИНЯТО, теперь здоровья: {player_xp}\n')
                    waiting()
                    break
        except ValueError:
            print(necor_zn())
    return settings()



def edit_exit():
    screen_clear()
    global sec_to_exit, customize_settings
    print('\n\t| (04) Изменение времени выхода |\n')
    print(f'\tСейчас, время выхода составляет: {sec_to_exit}')
    while True:
        print('\tВыберите время (в секундах) для отключения/перезапуска программы >> ', end='')
        sec_ex = input()
        try:
            if type(float(sec_ex)) == float:
                sec_to_exit = int(sec_ex)
                customize_settings = True
                Achieve.customize_set += 1
                print(f'\n\tПРИНЯТО, теперь время выключения/перезагрузки составит: {sec_to_exit} сек.\n')
                waiting()
            break
        except ValueError:
            print(necor_zn())
    return settings()


def edit_zastavka():
    screen_clear()
    global number_intro, customize_settings
    print('\n\t| (05) Выбор варианта заставки игры. |')
    while True:
        print('\t\t╞>"1" - Альфа-версия заставки')
        print('\t\t╞>"2" - Большая заставка')
        print('\t\t╘>"3" - Новая заставка (рекомендуется)\n')
        print('\tВыберите вариант желаемой заставки >> ', end='')
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
    print('\n\t\t---/===/ НАСТРОЙКИ \===\---\n')
    print('\tВозможные действия:')
    print('\t\t╞>"1" - Выбор количества уровней')
    print('\t\t╞>"2" - Выбор количества подсказок')
    print('\t\t╞>"3" - Выбор количества здоровья')
    print('\t\t╞>"4" - Изменение времени выхода')
    print('\t\t╞>"5" - Выбор варианта заставки')
    print('\t\t╘>"0" - Вкл./Выкл. Обновления экрана')
    print('\n\t*Все остальные команды перезапускают игру\n')
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
            print('\n\tВЫКЛючено обновление экрана\n')
            Achieve.ochistka = False
        else:
            ochist = True
            print('\n\tВКЛючено обновление экрана\n')
            if not Achieve.ochistka:
                Achieve.ochistka2 = True
        waiting()
    return ''


def about_credits():
    screen_clear()
    print('\n\t\t---/===/ От автора \===\---\n')
    print('\tЗдравствуй игрок, если ты видишь это сообщение, значит ты не случайно сюда зашёл.')
    print('\tБлагодарю тебя за выбор и запуск игры, в частности именно "От автора".')
    print('\tЭто то самое окошко в котором я могу в одностороннем порядке пожелать тебе удачной игры.')
    print('\n\t(PS: попробуй ввести "10" в главном меню ;)\n')
    credits_choose = input('\t>>')
    if credits_choose == '10':
        print('\tДа не здесь! (^-^")')
        sleep(2)
        Achieve.ten = True
    Achieve.creditss = True
    return ''


def dostyagi():
    screen_clear()
    global number_zapusk, sum_win, sum_nichya, sum_game_over
    print('\n\t\t---/===/ ДОСТИЖЕНИЯ \===\---\n')
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

    print('\n\tНЕСТАНДАРТНЫЕ:')
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

    print('\n\tРЕДКИЕ:')
    if Achieve.ten:
        print(f'\t╠═> ^-^: Увидеть микро-пасхалку в разделе "От автора" ({Achieve.customize_set })')
    else:
        print('\t╟')
    if Achieve.logo:
        print(f'\t╚═> ВПЕЧАТЛЁН?: "Выбрать" пасхалку "10" в Главном меню')
    else:
        print('\t╙')
    print('')
    print('\tКОДЕРОВСКАЯ:\taka. (OPEN-SOURCE code)')
    if Achieve.hello_world:
        print(f'\t╚═> МЕГАХОРОШ: Поменять переменную в окончании файла игры')
    else:
        print('\t╙X','Найди "hello_world" в 660+ строке кода.') # Пофикси ;)
    print('')
    waiting()
    return ''


def stats():
    screen_clear()
    global sum_win, sum_nichya, sum_game_over, number_zapusk
    print('\n\t---/===/ СТАТИСТИКА \===\---')
    print(f'\t\t ╟ПОБЕД:{sum_win}')
    print(f'\t\t ╟ВНИЧЬЮ:{sum_nichya}')
    print(f'\t\t ╟ПОРАЖЕНИЙ:{sum_game_over}')
    print('\t\t ║')
    print(f'\t\t ╙ЗАПУСКОВ ПРОГРАММЫ:{number_zapusk}')
    print('')
    waiting()
    return ''


def itogi_game(vern,nevern):
    global sum_win, sum_game_over, sum_nichya
    print('\t---===/ ИТОГИ ИГРЫ \===---')
    print(f'\t\tПОБЕД: {vern}')
    print(f'\t\tПОРАЖЕНИЙ: {nevern}')
    print('\t\tПОТОМУ', end='-->')
    if vern == nevern:
        print("НИЧЬЯ")
        print('\t\t\t\t:|')
        sum_nichya += 1
    elif vern > nevern:
        print('ПОБЕДА!')
        print('\t\t\t\t:)')
        sum_win += 1
    else:
        print('ПОРАЖЕНИЕ')
        print('\t\t\t\t:(')
        sum_game_over += 1
    return ''


def classic_game():
    screen_clear()
    global default_levels, player_levels

    print('\n---/===/\tКЛАССИЧЕСКАЯ ИГРА\t\===\---\n')
    print('\tКоличество уровней')
    if default_levels == player_levels:
        print(f'\t(установлено по умолчанию): {default_levels}')
        lvl = default_levels
    else:
        print(f'\tв соответствии с пользовательской настройкой: {player_levels}')
        lvl = player_levels
    print('\n\t\tПОЕХАЛИ!\n')

    vern = 0
    nevern = 0
    for level in range(1,lvl+1):
        print(f'\n\t╔═══\t-=| УРОВЕНЬ {level} |=-\t═══╗')
        choice_choose = input('\t║Ваше число >>\t')
        randomize = str(randint(0, 1))
        print(f'\t║Рандом = \t{randomize}')
        if choice_choose == randomize:
            print('\t║ВЕРНО!\t\t√  ')
            vern += 1
        else:
            print('\t║НЕВЕРНО.\tX  ')
            nevern += 1
        print(f'\t╚═══\t-=| УРОВЕНЬ {level} |=-\t═══╝\n')
        waiting()
        screen_clear()
    sleep(1)
    print(itogi_game(vern,nevern))
    waiting()


def all_or_nothing():
    screen_clear()
    global default_levels, player_levels

    print('\n---/===/  РЕЖИМ ИГРЫ: "ВСЁ ИЛИ НИЧЕГО"  \===\---\n')
    print('\tКоличество уровней')
    if default_levels == player_levels:
        print(f'\t(установлено по умолчанию): {default_levels}')
        lvl = default_levels
    else:
        print(f'\tв соответствии с пользовательской настройкой: {player_levels}')
        lvl = player_levels

    print('\n\t\tПОЕХАЛИ!\n')
    numer = input('Ваше число >> ')

    vern = 0
    nevern = 0
    print(f'╔════\t\t-=| ВСЁ ИЛИ НИЧЕГО |=-\t   ════╗')
    print('║\t| Ур.\t| №\t| Сл.Ч.\t| +/-  |       ║')
    for level in range(1, lvl + 1):
        randomize = str(randint(0, 1))
        print(f'║\t| {level}\t| {numer}\t| {randomize}\t|',end=' ')
        if numer == randomize:
            print(' √   |       ║')
            vern += 1
        else:
            print(' X   |       ║')
            nevern += 1
        sleep(0.1)
    print(f'╚════\t════════════════════════════════   ════╝')
    print('')
    sleep(1)
    print(itogi_game(vern,nevern))
    waiting()


def podskaz_game():
    screen_clear()
    global default_levels, player_levels
    global default_podskaz, player_podskaz

    print('\n---/===/\tИГРА С ПОДСКАЗКАМИ!\t\===\---\n')
    print(f'\tПодсказки будут появляться раз в ')
    if default_podskaz == player_podskaz:
        print(f'\t(установлено по умолчанию): {default_podskaz} ур.')
        pods = default_podskaz
    else:
        print(f'\t(в соответствии с пользовательской настройкой): {player_podskaz} ур.')
        pods = player_podskaz
    print('\n\tКоличество уровней')
    if default_levels == player_levels:
        print(f'\t(установлено по умолчанию): {default_levels}')
        lvl = default_levels
    else:
        print(f'\t(в соответствии с пользовательской настройкой): {player_levels}')
        lvl = player_levels
    print('\n\t\tПОЕХАЛИ!\n')

    vern = 0
    nevern = 0

    for level in range(1, lvl + 1):
        print(f'\n\t╔═══\t-=| УРОВЕНЬ {level} |=-\t═══╗')
        if level % pods == 0:
            randomize = str(randint(0, 1))
            print(f'\t║РАНДОМ = \t{randomize}')
            podskaz_choose = input('\t║Ваше число !!\t')

        else:
            podskaz_choose = input('\t║Ваше число >>\t')
            randomize = str(randint(0, 1))
            print(f'\t║Рандом = \t{randomize}')

        if podskaz_choose == randomize:
            print('\t║ВЕРНО!\t\t√  ')
            vern += 1
        else:
            print('\t║НЕВЕРНО.\tX  ')
            nevern += 1
        print(f'\t╚═══\t-=| УРОВЕНЬ {level} |=-\t═══╝\n')
        waiting()
        screen_clear()
    sleep(1)
    print(itogi_game(vern,nevern))
    waiting()


def xp_game():
    screen_clear()
    global default_xp, player_xp

    print('\n---/===/\tРежим игры "ЖИЗНИ"\t\===\---\n')
    print('\tКоличество здоровья')
    if default_xp == player_xp:
        print(f'\t(установлено по умолчанию):')
        print(f'\t\t{default_xp}', '♥' * default_xp)
        xp = default_xp
    else:
        print(f'\t(в соответствии с пользовательской настройкой):')
        print(f'\t\t{player_xp}', '♥' * player_xp)
        xp = player_xp
    print('\n\t\tПОЕХАЛИ!\n')

    vern = 0
    nevern = 0
    level = 0
    while xp > 0:
        level += 1
        print('\t\t',f'{xp}','♥'*xp)
        print(f'\t╔═══\t-=|  УРОВЕНЬ {level}   |=-\t═══╗')
        xp_choose = input('\t║Ваше число >>\t')
        randomize = str(randint(0, 1))
        print(f'\t║Рандом = \t{randomize}')
        if xp_choose == randomize:
            print('\t║ВЕРНО!\t\t√  ')
            vern += 1
        else:
            print('\t║НЕВЕРНО.\tX  ')
            nevern += 1
            xp -= 1
        print(f'\t╚═══\t-=| Здоровья: {xp}♥ |=-\t═══╝')
        waiting()
        screen_clear()
    print('\n\tЗДОРОВЬЕ ЗАКОНЧИЛОСЬ!\n')
    sleep(0.5)
    print(itogi_game(vern, nevern))
    waiting()



# ОСНОВА
base = 'teleport'
while game_restart:
    screen_clear()
    start_window()
    print('\n---/===/\tДОБРО ПОЖАЛОВАТЬ!\t\===\---\n')
    if number_zapusk == 1:
        print('\tИгра запущена первый раз!')
        print('\tНе желаете ли прочесть Справку?')
        print('\tНажмите "5" для вызова Справки\n')
    print('\t---/===/  ГЛАВНОЕ МЕНЮ:  \===\---\t')
    print('\tВозможные действия:')
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
    print('\n\t*Все остальные команды перезапускают игру',end='')
    Achieve.hello_world = False     # Вот этот 'hello_world' ;)
    if not Achieve.logo:
        print('')
    else:
        print('**\t\t**Почти все ;)')
    choose = input('\t>>')
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
        screen_clear()
        print('\tПожалуйста, увеличь размер окна игры,')
        print('\tтак ты увидишь то, что нужно ;)')
        input('\tВведи что-нибудь как будешь готов >> ')
        graphics(10)
        Achieve.logo = True
        choose = input('\t>> ')
        if choose == '10':
            print('Ну шаришь-шаришь! \Оꞈо/ ')
            sleep(1)
    else:
        continue
