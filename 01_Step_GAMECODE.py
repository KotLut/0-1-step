# ИМПОРТ:
from time import sleep
from random import randint
from os import name, system


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


# ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ:
default_levels = 10
default_podskaz = 4
default_xp = 5
customize_settings = False
game_restart = True

# ИЗМЕНЯЕМЫЕ ПЕРЕМЕННЫЕ
number_zapusk = 0
sec_to_exit = 3
player_levels = 10
player_podskaz = 4
player_xp = 5
number_intro = 3
ochist = True
sum_win = 0
sum_nichya = 0
sum_game_over = 0

# КЛАСС АЧИВОК
class Achieve:
    customize_set = 0
    old_win = 0
    big_win = 0
    ochistka = 0
    ochistka2 = 0
    creditss = 0
    logo = 0
    ten = 0
    hello_world = 0

# ФУНКЦИИ:
def screen_clear():
    if ochist == 1:
        if name == 'nt': # Windows
            system('cls')
        elif name == 'posix':    # Unix (Linux or macOS)
            system('clear')


def necor_zn():
    return '\n\t| ВВЕДЕННО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ! |\n'


def waiting():
    return input('\tВведите что-нибудь, чтобы продолжить >> ')

# СОХРАНЕНИЯ
def safe_wr(wr):
    global number_zapusk
    global sec_to_exit
    global player_levels
    global player_podskaz
    global player_xp
    global number_intro
    global ochist
    global sum_win
    global sum_nichya
    global sum_game_over
    if wr == 1:
        with open('save_data.txt','w',encoding='utf-8') as f3:
            f3.writelines(f'{number_zapusk}\n')
            f3.writelines(f'{sec_to_exit}\n')
            f3.writelines(f'{player_levels}\n')
            f3.writelines(f'{player_podskaz}\n')
            f3.writelines(f'{player_xp}\n')
            f3.writelines(f'{number_intro}\n')
            f3.writelines(f'{int(ochist)}\n')
            f3.writelines(f'{sum_win}\n')
            f3.writelines(f'{sum_nichya}\n')
            f3.writelines(f'{sum_game_over}\n')

            f3.writelines(f'{Achieve.customize_set}\n')
            f3.writelines(f'{Achieve.old_win}\n')
            f3.writelines(f'{Achieve.big_win}\n')
            f3.writelines(f'{Achieve.ochistka}\n')
            f3.writelines(f'{Achieve.ochistka2}\n')
            f3.writelines(f'{Achieve.creditss}\n')
            f3.writelines(f'{Achieve.logo}\n')
            f3.writelines(f'{Achieve.ten}\n')
            f3.writelines(f'{int(Achieve.hello_world)}\n')

            f3.close()
        return print('\n\t\t\tСОХРАНЕНИЕ ЗАПИСАНО!\n')

    elif wr == 2:
        with open('save_data.txt', 'r', encoding='utf-8') as f2:
            number_zapusk = int(f2.readline())
            sec_to_exit = int(f2.readline())
            player_levels = int(f2.readline())
            player_podskaz = int(f2.readline())
            player_xp = int(f2.readline())
            number_intro = int(f2.readline())
            ochist = bool(f2.readline())
            sum_win = int(f2.readline())
            sum_nichya = int(f2.readline())
            sum_game_over = int(f2.readline())

            Achieve.customize_set = int(f2.readline())
            Achieve.old_win = int(f2.readline())
            Achieve.big_win = int(f2.readline())
            Achieve.ochistka = int(f2.readline())
            Achieve.ochistka2 = int(f2.readline())
            Achieve.creditss = int(f2.readline())
            Achieve.logo = int(f2.readline())
            Achieve.ten = int(f2.readline())
            Achieve.hello_world = bool(f2.readline())

            f2.close()
        return print('\n\t\t\tСЧИТАНО СОХРАНЕНИЕ!\n')

    else:
        with open('save_data.txt','w',encoding='utf-8') as f3:
            f3.writelines(f'{1}\n')     # number_zapusk
            f3.writelines(f'{3}\n')     # sec_to_exit
            f3.writelines(f'{10}\n')    # player_levels
            f3.writelines(f'{4}\n')     # player_podskaz
            f3.writelines(f'{5}\n')     # player_xp
            f3.writelines(f'{3}\n')     # number_intro
            f3.writelines(f'{1}\n')     # ochist
            f3.writelines(f'{0}\n')     # sum_win
            f3.writelines(f'{0}\n')     # sum_nichya
            f3.writelines(f'{0}\n')     # sum_game_over

            f3.writelines(f'{0}\n')     # customize_set
            f3.writelines(f'{0}\n')     # old_win
            f3.writelines(f'{0}\n')     # big_win
            f3.writelines(f'{0}\n')     # ochistka
            f3.writelines(f'{0}\n')     # ochistka2
            f3.writelines(f'{0}\n')     # creditss
            f3.writelines(f'{0}\n')     # logo
            f3.writelines(f'{0}\n')     # ten
            f3.writelines(f'{0}\n')     # hello_world
        return print('\n\t\t\tСОХРАНЕНИЕ "ПО-УМОЛЧАНИЮ"!\n')


def graphics(num):
    if num == 1:
        old_s_win = graphica[0:9]
        for wind in old_s_win:
            wind = wind.replace('\n', '')
            sleep(0.002)
            print('\t\t',wind)
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
        print('\n\t\t| НАСТРОЙКИ ПРИМЕНЕНЫ! |\n')
        sleep(1)
        customize_settings = False
    elif number_zapusk < 1:
        print('\n\t\t| ЗАПУСК ИГРЫ |\n')
    else:
        print('\n\t\t| ПЕРЕЗАГРУЗКА... |\n')
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
    print('\n\t\t   |   ЗАПУСК   |')
    print(f'\t\t   |   № {number_zapusk}\t|')


def global_exit():
    screen_clear()
    global game_restart, sec_to_exit
    game_restart = False
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


def spravka():
    screen_clear()
    print('\n\t\t---/===/  СПРАВКА  \\===\\---\n')
    print('\tСправка появится в следущем обновлении!')
    print('\tПока, просьба, читать сообщения игры')
    print('\t ;) ')
    waiting()


def edit_level():
    screen_clear()
    global default_levels, player_levels, customize_settings
    print('\n\t| (01) Выбор количества уровней |\n')
    if default_levels == player_levels:
        print(f'\tУровней по умолчанию: {default_levels}')
    else:
        print(f'\tУровней выбрано ранее: {player_levels}')
    while True:
        pl_levels = input('\tВыберите желаемое количество уровней: ')
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
        pl_podsk = input('\tВыберите частоту подсказок на уровнях: ')
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
        pl_xp = input('\tВыберите количество здоровья на уровнях: ')
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
        sec_ex = input('\tВыберите время (в секундах) для отключения/перезапуска программы: ')
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
        print('\t\t╘>"3" - Новая заставка (рекомендуется)')
        zast = input('\n\tВыберите вариант желаемой заставки >> ')
        try:
            if type(int(zast)) == int:
                number_intro = int(zast)
                customize_settings = True
                Achieve.customize_set += 1
                print(f'ПРИНЯТО, выбрана заставка номер: {number_intro}.')
            break
        except ValueError:
            print(necor_zn())
    waiting()
    return settings()


def edit_saves():
    screen_clear()
    if choose == '11':
        print('\n\t\t| БЫСТРЫЙ ВЫЗОВ ДЕЙСТВИЙ СОХРАНЕНИЙ |')
        print('\t   (быстрый переход для продвинутых пользователей)')
    global customize_settings
    print('\n\t\t| (11) Действия с СОХРАНЕНИЕМ ИГРЫ  |')
    print('\t\t\t╞>"1" - Запись текущего прогресса')
    print('\t\t\t╞>"2" - Чтение сохранения')
    print('\t\t\t╘>"3" - Запись данных "по-умолчанию" в сохранение')
    print('\t\t\t        *Это не изменит данные текущей игры')
    print('\n\t\tВыберите действие с сохранением >> ', end='')
    sohr = input()
    if sohr == '1':
        safe_wr(1)
    elif sohr == '2':
        safe_wr(2)
    elif sohr == '3':
        safe_wr(3)
    else:
        print('\n\t\t\tНичего не изменено!\n')
    waiting()
    if choose != '11':
        return settings()


def settings():
    global ochist
    screen_clear()
    print('\n\t\t---/===/ НАСТРОЙКИ \\===\\---\n')
    print('\tВозможные действия:')
    print('\t\t║ ╞>"1" - Выбор количества уровней')
    print('\t\t║ ╞>"2" - Выбор количества подсказок')
    print('\t\t║ ╞>"3" - Выбор количества здоровья')
    print('\t\t║ ╞>"4" - Изменение времени выхода')
    print('\t\t║ ╞>"5" - Выбор варианта заставки')
    print('\t\t║ ╘>"0" - Вкл./Выкл. Обновления экрана')
    print('\t\t╚═>"11" - Действия с СОХРАНЕНИЕМ')
    print('\n\t*Все остальные команды перезапускают игру')
    settings_choose = input('\n\t>>')
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
            Achieve.ochistka = 1
        else:
            ochist = True
            print('\n\tВКЛючено обновление экрана\n')
            if Achieve.ochistka > 0:
                Achieve.ochistka2 = 1
        waiting()
    elif settings_choose == '11':
        print(edit_saves())


def stats():
    screen_clear()
    global sum_win, sum_nichya, sum_game_over, number_zapusk
    print('\n\t---/===/ СТАТИСТИКА \\===\\---')
    print(f'\t\t ╟ПОБЕД:{sum_win}')
    print(f'\t\t ╟ВНИЧЬЮ:{sum_nichya}')
    print(f'\t\t ╟ПОРАЖЕНИЙ:{sum_game_over}')
    print('\t\t ║')
    print(f'\t\t ╙ЗАПУСКОВ ПРОГРАММЫ:{number_zapusk}')
    print('')
    waiting()


def dostyagi():
    screen_clear()
    global number_zapusk, sum_win, sum_nichya, sum_game_over
    print('\n\t\t---/===/ ДОСТИЖЕНИЯ \\===\\---\n')
    print('\tКЛАССИЧЕСКИЕ:')
    if number_zapusk > 10:
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
    if Achieve.ochistka > 0:
        print(f'\t╠═> ЛИНИЯМИ: Убрать автоочистку aka. ВЫКЛючить автообновление экрана')
    else:
        print('\t╟')
    if Achieve.ochistka2 > 0:
        print(f'\t╠═> ТАК_ЛУЧШЕ: Всё-таки включить автооичтску aka. снова ВКЛючить автообновление экрана')
    else:
        print('\t╟')
    if Achieve.creditss > 0:
        print(f'\t╚═> ЧИТАТЕЛЬ: Посмотреть раздел "От автора"')
    else:
        print('\t╙')

    print('\n\tРЕДКИЕ:')
    if Achieve.ten > 0:
        print(f'\t╠═> ^-^: Увидеть микро-пасхалку в разделе "От автора" ({Achieve.customize_set })')
    else:
        print('\t╟')
    if Achieve.logo > 0:
        print(f'\t╚═> ВПЕЧАТЛЁН?: "Выбрать" пасхалку "10" в Главном меню')
    else:
        print('\t╙')
    print('')
    print('\tКОДЕРОВСКАЯ:\taka. (OPEN-SOURCE code)')
    if Achieve.hello_world > 0:
        print(f'\t╚═> МЕГАХОРОШ: Поменять переменную в окончании файла игры')
    else:
        print('\t╙X','Найди "hello_world" в 660+ строке кода.') # Пофикси ;)
    print('')
    waiting()


def about_credits():
    screen_clear()
    print('\n\t\t---/===/ От автора \\===\\---\n')
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


def itogi_game(vern,nevern):
    global sum_win, sum_game_over, sum_nichya
    print('\t---===/ ИТОГИ ИГРЫ \\===---')
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

    print('\n---/===/\tКЛАССИЧЕСКАЯ ИГРА\t\\===\\---\n')
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

    print('\n---/===/  РЕЖИМ ИГРЫ: "ВСЁ ИЛИ НИЧЕГО"  \\===\\---\n')
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

    print('\n---/===/\tИГРА С ПОДСКАЗКАМИ!\t\\===\\---\n')
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

    print('\n---/===/\tРежим игры "ЖИЗНИ"\t\\===\\---\n')
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
    print('\n---/===/\tДОБРО ПОЖАЛОВАТЬ!\t\\===\\---\n')
    if number_zapusk == 1:
        print('\tИгра запущена первый раз!')
        print('\tНе желаете ли прочесть Справку?')
        print('\tНажмите "5" для вызова Справки\n')
    print('\t---/===/  ГЛАВНОЕ МЕНЮ:  \\===\\---\t')
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
        classic_game()
    elif choose == '2':
        all_or_nothing()
    elif choose == '3':
        xp_game()
    elif choose == '4':
        podskaz_game()
    elif choose == '5':
        spravka()
    elif choose == '6':
        settings()
    elif choose == '7':
        stats()
    elif choose == '8':
        dostyagi()
    elif choose == '9':
        about_credits()
    elif choose == '0':
        global_exit()
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
    elif choose == '11':
        edit_saves()
    else:
        continue
