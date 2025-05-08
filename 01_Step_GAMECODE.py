# v0.9a 01_Step
# ИМПОРТ:
from time import sleep
from random import randint
from os import name, system
import webbrowser as web

# ФУНКЦИЯ ОЖИДАНИЯ действий от игрока. Нужна именно здесь, на случай ошибок.
def waiting():
    return input('\tВведите что-нибудь, чтобы продолжить >> ')


# ПРОВЕРКА ГРАФИКИ и ИМПОРТ ГРАФИКИ
try:
    graphica = open('graphicsASC.txt', encoding='utf-8', errors='ignore').readlines()
except FileNotFoundError:
    print('''\n\t\tГРАФИКА ИГРЫ НЕ ЗАГРУЖЕНА!\n
    \tВозможно вы запускаете Игру из Архива,
    \tтогда разархивируйте папку. Иначе
    \tпросьба подтянуть файл "graphicsASC.txt"
    \tв папку с этим файлом и перезапустить Игру!\n''')
    graphica = ['// Здесь должна быть графика! //']*170
    waiting()


# ПРОВЕРКА СОХРАНЕНИЙ
try:
    saves = open('save_data.txt', encoding='utf-8').readlines()
    save_error = False
except FileNotFoundError:
    print('''\n\t\tФАЙЛ СОХРАНЕНИЙ НЕ ОБНАРУЖЕН!\n
    \tВозможно вы запускаете Игру из Архива,
    \tтогда разархивируйте папку. Иначе
    \tпросьба подтянуть файл "save_data.txt"
    \tв папку с этим файлом и перезапустить Игру!\n''')
    save_error = True
    waiting()

# ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ:
default_levels = 10
default_podskaz = 4
default_xp = 5
customize_settings = False
game_restart = True
link = 'https://raw.githubusercontent.com/KotLut/01_Step/refs/heads/main/01_Step_alpha-logo.png'

# ИЗМЕНЯЕМЫЕ ПЕРЕМЕННЫЕ
number_zapusk = 0
sec_to_exit = 3
player_levels = 10
player_podskaz = 4
player_xp = 5
number_intro = 3
ochist = 1
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
    watch_saves = 0
    link_open = 0
    logo2 = 0
    zap3 = 0
    zap4 = 0
    zap5 = 0

# ФУНКЦИИ:
def screen_clear():
    if ochist == 1:
        if name == 'nt': # Windows
            system('cls')
        elif name == 'posix':    # Unix (Linux or macOS)
            system('clear')


def necor_zn():
    return '\n\t| ВВЕДЕННО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ! |\n'


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
        if save_error:
            return print('\n\t\t\tСОХРАНЕНИЕ НЕ ЗАПИСАНО!\n\n\t\t\tТак как ФАЙЛ СОХРАНЕНИЯ НЕ ОБНАРУЖЕН.\n')
        else:
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
                f3.writelines(f'{Achieve.watch_saves}\n')
                f3.writelines(f'{Achieve.link_open}\n')
                f3.writelines(f'{Achieve.logo2}\n')
                f3.writelines(f'{Achieve.zap3}\n')
                f3.writelines(f'{Achieve.zap4}\n')
                f3.writelines(f'{Achieve.zap5}\n')

                f3.close()
            return print('\n\t\t\tСОХРАНЕНИЕ ЗАПИСАНО!\n')

    elif wr == 2:
        if save_error:
            return print('\n\t\t\tСОХРАНЕНИЕ НЕ СЧИТАНО!\n\n\t\t\tТак как ФАЙЛ СОХРАНЕНИЯ НЕ ОБНАРУЖЕН.\n')
        else:
            with open('save_data.txt', 'r', encoding='utf-8') as f2:
                number_zapusk = int(f2.readline())
                sec_to_exit = int(f2.readline())
                player_levels = int(f2.readline())
                player_podskaz = int(f2.readline())
                player_xp = int(f2.readline())
                number_intro = int(f2.readline())
                ochist = int(f2.readline())
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
                Achieve.hello_world = int(f2.readline())
                Achieve.watch_saves = int(f2.readline())
                Achieve.link_open = int(f2.readline())
                Achieve.logo2 = int(f2.readline())
                Achieve.zap3 = int(f2.readline())
                Achieve.zap4 = int(f2.readline())
                Achieve.zap5 = int(f2.readline())

                f2.close()
            return print('\n\t\t\tСЧИТАНО СОХРАНЕНИЕ!\n')

    else:
        if save_error:
            return print('\n\t\t\tДАННЫЕ "ПО-УМОЛЧАНИЮ" НЕ ЗАПИСАНЫ В СОХРАНЕНИЕ!'
                         '\n\n\t\t\tТак как ФАЙЛ СОХРАНЕНИЯ НЕ ОБНАРУЖЕН.\n')
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
                f3.writelines(f'{0}\n')     # watch_saves
                f3.writelines(f'{0}\n')     # zap1
                f3.writelines(f'{0}\n')     # zap2
                f3.writelines(f'{0}\n')     # zap3
                f3.writelines(f'{0}\n')     # zap4
                f3.writelines(f'{0}\n')     # zap5

                f3.close()
            return print('\n\t\t\tСОХРАНЕНИЕ "ПО-УМОЛЧАНИЮ"!\n')


def graphics(num):
    if num == 1:
        old_s_win = graphica[0:9]
        for wind in old_s_win:
            wind = wind.replace('\n', '')
            sleep(0.002)
            print('\t\t',wind)
    elif num == 2:
        big_s_win = graphica[10:55]
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
        if Achieve.logo and Achieve.link_open:
            new_s_win = graphica[170:251]
            print(*new_s_win)
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


def exit_global():
    screen_clear()
    global game_restart, sec_to_exit
    game_restart = False
    print('''\n\t|    ИНИЦИАЛИЗИРОВАН\t|
    \t|  ВЫХОД ИЗ ПРОГРАММЫ!\t|
    \tПРОГРАММА ЗАКРОЕТСЯ ЧЕРЕЗ:''')
    for seconds in range(sec_to_exit, 0, -1):
        if seconds == 1:
            print(f'\t     {seconds}\tсекунду')
        elif 1 < seconds <= 3:
            print(f'\t     {seconds}\tсекунды')
        else:
            print(f'\t     {seconds}\tсекунд')
        sleep(1)


def spr_classik_game():
    screen_clear()
    print('''\n\t\t| (1) Подробности о Классической игре |\n
            Это основной режим Игры. Его геймплей заключается в следущем:
        на каждом уровне вы выбираете цифру "0" или "1", и если ваш ответ
        совпадает с цифрой, которая случайно выбранна компьютером, то
        уровень считается верным, то есть выигранным.
            Если ответ не совпадает с случайным числом, то уровень считается
        проигранным.
            В конце кажой игры выводятся итоги игры, которые, исходя из количества
        верных и неверных ответов засчитывают игроку:
            - "ПОБЕДУ" - если количество верных уровней больше, чем неверных;
            - "НИЧЬЮ" - если количество верных равно кол-ву неверных;
            - "ПОРАЖЕНИЕ" - если неверных уровней больше, чем верных.
            
            Эти данные сохраняются и учитываются в блоках "Статистика" и "Достижения".
        Количество уровней можно изменить в Настройках Игры.
            Подробнее об этом, вы можете прочитать в соседних разделах Справки:
        "Подробности о Настройках", "Подробности о Статистике" и "Подробности о Достижениях".
        
            \n''')
    waiting()
    return spravka()


def spr_all_or_nothing():
    screen_clear()
    print('''\n\t\t| (2) Подробности о режиме "Всё или ничего" |\n
            Это режим Игры, в котором вам предстоит выбрать одну цифру
        "0" или "1" и она будет автоматически введена во все уровни, и если
        ваш ответ на уровне совпадает с цифрой, которая случайно была выбранна
        компьютером, то уровень считается верным, то есть выигранным.
            Если ответ не совпадает с случайным числом, то уровень считается
        проигранным.
        
            Все уровни этого режима отображаются таблицей, где строки - это уровни,
        а столбцы обозначают следущее:
            - "№ Ур." - номер уровня;
            - "Ваш.Ч." - введенное вами число;
            - "Сл.Ч." - выбранное компьютером число;
            - "+/-" - соответствует ли ваше значение случайному числу:
                      "√" - если значения совпадают, иначе - "X".
        
            В конце кажой игры выводятся итоги игры, которые, исходя из количества
        верных и неверных ответов засчитывают игроку:
            - "ПОБЕДУ" - если количество верных уровней больше, чем неверных;
            - "НИЧЬЮ" - если количество верных равно кол-ву неверных;
            - "ПОРАЖЕНИЕ" - если неверных уровней больше, чем верных.
            
            Эти данные сохраняются и учитываются в блоках "Статистика" и "Достижения".
        Количество уровней можно изменить в настройках Игры.
            Подробнее об этом, вы можете прочитать в соседних разделах Справки:
        "Подробности о Настройках", "Подробности о Статистике" и "Подробности о Достижениях".
            \n''')
    waiting()
    return spravka()


def spr_xp_game():
    screen_clear()
    print('''\n\t\t| (3) Подробности о режиме Игры "ЖИЗНИ" |\n
            Это режим Игры, сходный с "Классическим", но тут ограничение на количество
        уровней задано количеством здоровья (♥).
            То-есть при верном ответе уровень здоровья остаётся тем же, но при неверном
        ответе отнимается 1 еденица здоровья (♥).
        
        В остальном правила аналогичны "Классическому" режиму.
        О них вы можете прочитать в соседнем разделе Справки - "Подробности о Классической игре".
        
            Количество здоровья можно регулировать в Настройках Игры.
         Подробнее об этом, вы можете прочитать в соседнем разделах Справки:
        "Подробности о Настройках".
            \n''')
    waiting()
    return spravka()


def spr_podskaz_game():
    screen_clear()
    global player_podskaz
    print(f'''\n\t\t| (4) Подробности о режиме Игры "С подсказками" |\n
            Это режим Игры, сходный с "Классическим", но тут есть подсказки!
        Да, специально для игрока введены подсказки, которые появляются с частотой
        раз в несколько ({player_podskaz}) уровней.
        Это значение можно изменить в Настройках.
        
            В остальном правила аналогичны "Классическому" режиму.
        О них вы можете прочитать в соседнем разделе Справки ("Классическая игра")
        
        А об изменении частоты подсказок можно прочесть в разделе Справки:
        "Подробности о Настройках".
            \n''')
    waiting()
    return spravka()


def spr_errors():
    screen_clear()
    print(f'''\n\t\t| (5) Подробности об ошибках при запуске Игры |\n
            Вылет сообщений типа "ГРАФИКА ИГРЫ НЕ ЗАГРУЖЕНА!" и/или "ФАЙЛ СОХРАНЕНИЙ НЕ ОБНАРУЖЕН!"
        свидетельствует о том, что файл(ы) "graphicsASC.txt" и/или "save_data.txt" соответственно
        не загружены в папку с исполняем кодом ("01_Step_GAMECODE.py").
            Во избежание таких сообщений, выполните следующие действия:
            1) Проверьте, разархивирована ли папка с Игрой. Если это не так, то распакуйте всё
              содержимое в одну папку.
            2) Проверьте наличие файлов "graphicsASC.txt" и "save_data.txt" в папке с исполняемым кодом.
            
            Это основные методы решения проблемы, в редких случаях ещё приходиться проверять расширение файла.
            В остальном, при правильном скачивании и извлечении файлов Игры, проблем возникнуть не должно.            
            \n''')
    waiting()
    return spravka()


def spr_settings():
    screen_clear()
    print(f'''\n\t\t| (6) Подробности о Настройках Игры |\n
            В Настройках вам доступно изменение количества:
            - уровней   (для игровых режимов, использующих количество уровней)
            - подсказок (только для режима "С подсказками")
            - здоровья  (только для режима "ЖИЗНИ")
            - времени выхода (из Игры (в секундах))
            - варианта заставки:
                - "1" - Альфа-версия заставки
                - "2" - Большая заставка
                - "3" - Новая заставка (рекомендуется и установлена по-умолчанию)
            - обновление экрана (вкл./выкл. автообновления экрана при многих действиях,
              в том числе и на уровнях)
            
            А также можно перейти на блок действий с сохранением Игры.
        Об этом подробнее можно прочитать в соседнем разделе Справки:
        "Подробности о сохранениях игры".
            Отдельно отмечу невозможность выбора ненатуральных значений при
        выборе каждой настройки.
            \n''')
    waiting()
    return spravka()


def spr_stats():
    screen_clear()
    print(f'''\n\t\t| (7) Подробности о Статистике |\n
            В Статистике вы можете увидеть информацию о количестве своих
        побед, поражений, а также об играх сыгранных вничью.
            В статистике учитываются все режимы игры.
            
            Статистика обновляется в соответствии с сохранениями.
            Она записывается и считывается.
            Более подробно о сохранениях Игры можно посмотреть в
            соседнем разделе Справки: "Подробности о сохранениях игры"
            \n''')
    waiting()
    return spravka()


def spr_dostyagi():
    screen_clear()
    print(f'''\n\t\t| (8) Подробности о Достижениях |\n
            В Достижениях вы можете посмотреть полученные вами внутриигровые достижения.
            Этот блок разделен на три раздела, с разным типом достижений в каждом:
            - "ОБЫКНОВЕННЫЕ", это те, что можно получить просто играя в игру. Нужно
              выигрывать, сыграть вничью, проигрывать, и просто перезапускать игру.
              Ничего сложного.
            - "НЕСТАНДАРТНЫЕ", это такой тип достижений, над которым нужно подумать.
              в основном они связаны с блоком Настроек.
            - "РЕДКИЕ". Эти достижения связаны непосредственно с "пасхалками" от автора.
              Попробуйте найти :)
            
            Отдельно сообщу о разделе достижений "КОДЕР". В нём всего одно достижение,
        но для его получения необходимо найти предпоследний "hello_world" в 1030+ строке кода
        и "пофиксить" это для достижения. Для этого нужно обладать базовыми знаниями о языке Игры
        (Python3).
        Потому оно и расположено ниже редких. Для настоящих энтузиастов ;)
            \n''')
    waiting()
    return spravka()


def spr_about_credits():
    screen_clear()
    print(f'''\n\t\t| (9) Подробности о блоке "От автора" |\n
            В блоке "От автора" вы можете прочитать небольшое напутствие от автора Игры.
            Также с ним связанно несколько "пасхалок", но это лишь небольша подсказка.
            Дальше - ищите сами :)
            \n''')
    waiting()
    return spravka()


def spr_exit():
    screen_clear()
    print(f'''\n\t\t| (0) Подробности о выходе из Игры |\n
            При вводе "0" в главном меню 01_Step начинает закрываться.
        Это происходит последовательно. С посекундным отсчетом.
        Для редактирования времени выхода воспользуйтесь настройками.
        Подробнее об этом можете прочесть в разделе Справки "Подробности о Настройках".
            \n''')
    waiting()
    return spravka()


def spr_saves():
    screen_clear()
    print(f'''\n\t\t| (11) Подробности о сохранениях Игры |\n
            При вводе "11" в главном меню можно быстро попасть в блок действий
        с сохранениями Игры. Также доступ к нему есть в Настройках Игры.\
        
            В блоке действий с сохранениями Игры вы можете ввести следущие команды:
            - "1": Запись текущего прогресса игры в сохранение
            - "2": Чтение прогресса из сохранения
            - "3": Возврат сохранения в состояние "По-умолчанию"
                   *Это действие не менят данные текущей игры!
                   
            Все эти действия позволяют вам сохранять свой прогресс в 01_Step.
            \n''')
    waiting()
    return spravka()


def spravka():
    screen_clear()
    print('\n\t\t---/===/\tСПРАВКА  \t\\===\\---\n')
    print('''\tВас приветствует справка по Игре "01_Step"!\n
        \tПодробности о:
        \t╠>"1" - "Классической игре"
        \t╠>"2" - режиме "Всё или ничего"
        \t╠>"3" - режиме "ЖИЗНИ"
        \t╠>"4" - режиме Игры "С подсказками"
        \t╠>"5" - ошибках при запуске Игры
        \t╠>"6" - Настройках
        \t╠>"7" - Статистике
        \t╠>"8" - Достижения
        \t╠═>"9" - блоке "От автора"
        \t╠>"0" - выходе из Игры
        \t╚>"11" - сохранениях Игры
        \n\t*Все остальные команды перезапускают Игру и возвращают в Главное меню\n''')
    spr_choose = input('\tО каком разделе вы хотите узнать подробности? >> ')
    if spr_choose == '1':
        spr_classik_game()
    elif spr_choose == '2':
        spr_all_or_nothing()
    elif spr_choose == '3':
        spr_xp_game()
    elif spr_choose == '4':
        spr_podskaz_game()
    elif spr_choose == '5':
        spr_errors()

    elif spr_choose == '6':
        spr_settings()
    elif spr_choose == '7':
        spr_stats()
    elif spr_choose == '8':
        spr_dostyagi()
    elif spr_choose == '9':
        spr_about_credits()
    elif spr_choose == '0':
        spr_exit()
    elif spr_choose == '11':
        spr_saves()
    else:
        print('')
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
            if int(pl_levels) <= 0:
                print(necor_zn())
            else:
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
    print('''\n\t| (02) Выбор количества подсказок |\n
    \t//Через какое кол-во уровней будут появляться подсказки
    \t\\\в режиме Игры "С подсказками".
    \t//"1" - означает частоту в каждый уровень. Чем больше,
    \t\\\значение, тем реже будет появляться подсказка.\n''')
    if default_podskaz == player_podskaz:
        print(f'\tЧастота подсказок по умолчанию: {default_podskaz}')
    else:
        print(f'\tЧастота подсказок, выбранная ранее: {player_podskaz}')
    while True:
        pl_podsk = input('\tВыберите частоту подсказок на уровнях: ')
        try:
            if int(pl_podsk) <= 0:
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
    print('\t//От здоровья зависит длительность режима Игры "ЖИЗНИ".')
    print('\t\\\Чем больше значение - тем дольше будет длиться игра.\n')
    if default_xp == player_xp:
        print(f'\tКоличество здоровья по умолчанию: {default_xp}')
    else:
        print(f'\tКоличество здоровья, выбранное ранее: {player_xp}')
    while True:
        pl_xp = input('\tВыберите количество здоровья на уровнях: ')
        try:
            if int(pl_xp) <= 0:
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
        sec_ex = input('\tВыберите время (в секундах) для отключения/перезапуска Игры: ')
        try:
            if int(sec_ex) <= 0:
                print(necor_zn())
            else:
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
    print('\n\t| (05) Выбор варианта заставки Игры. |')
    while True:
        print('''\t\t╞>"1" - Альфа-версия заставки
        \t╞>"2" - Большая заставка
        \t╘>"3" - Новая заставка (рекомендуется)''')
        zast = input('\n\tВыберите вариант желаемой заставки >> ')
        try:
            if type(int(zast)) == int:
                if int(zast) < 1 or int(zast) > 3:
                    print(necor_zn())
                else:
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
    print('''\n\t\t| (11) Действия с СОХРАНЕНИЕМ ИГРЫ  |
    \t\t\t╞>"1" - Запись текущего прогресса
    \t\t\t╞>"2" - Чтение сохранения
    \t\t\t╘>"3" - Запись данных "по-умолчанию" в сохранение
    \t\t\t        *Это не изменит данные текущей Игры''')
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
    Achieve.watch_saves = 1
    waiting()
    if choose != '11':
        return settings()


def settings():
    global ochist
    screen_clear()
    print('\n\t\t---/===/ НАСТРОЙКИ \\===\\---\n')
    print('''\t\tВозможные действия:
    \t\t║ ╞>"1" - Выбор количества уровней
    \t\t║ ╞>"2" - Выбор количества подсказок
    \t\t║ ╞>"3" - Выбор количества здоровья
    \t\t║ ╞>"4" - Изменение времени выхода
    \t\t║ ╞>"5" - Выбор варианта заставки
    \t\t║ ╘>"0" - Вкл./Выкл. Обновления экрана
    \t\t╚═>"11" - Действия с СОХРАНЕНИЕМ
    \n\t*Все остальные команды перезапускают Игру и возвращают в Главное меню''')
    settings_choose = input('\n\tВыбор действия >> ')
    if settings_choose == '1':
        edit_level()
    elif settings_choose == '2':
        edit_podskazka()
    elif settings_choose == '3':
        edit_xp()
    elif settings_choose == '4':
        edit_exit()
    elif settings_choose == '5':
        edit_zastavka()
    elif settings_choose == '0':
        if ochist:
            ochist = 0
            print('\n\tВЫКЛючено обновление экрана\n')
            Achieve.ochistka = 1
        else:
            ochist = 1
            print('\n\tВКЛючено обновление экрана\n')
            if Achieve.ochistka > 0:
                Achieve.ochistka2 = 1
        waiting()
    elif settings_choose == '11':
        edit_saves()
    else:
        waiting()


def stats():
    screen_clear()
    global sum_win, sum_nichya, sum_game_over, number_zapusk
    print('\n\t---/===/ СТАТИСТИКА \\===\\---')
    print(f'''\t\t ╟ПОБЕД:{sum_win}
    \t\t ╟ВНИЧЬЮ:{sum_nichya}
    \t\t ╟ПОРАЖЕНИЙ:{sum_game_over}
    \t\t ║
    \t\t ╙ЗАПУСКОВ ПРОГРАММЫ:{number_zapusk}
    ''')
    waiting()


def dostyagi():
    screen_clear()
    global number_zapusk, sum_win, sum_nichya, sum_game_over
    print('\n\t\t---/===/ ДОСТИЖЕНИЯ \\===\\---\n')
    print('\tОБЫКНОВЕННЫЕ:')
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
    if Achieve.watch_saves > 0:
        print(f'\t╠═> CОХРАНИТЬ: Побывать в меню сохранений')
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
        print(f'\t╠═> ВПЕЧАТЛЁН?: "Выбрать" пасхалку "10" в Главном меню')
    else:
        print('\t╟')
    if Achieve.logo2 > 0:
        print(f'\t╠═> АВТОР_ШУТИТ: Увидеть альтернативную аватарку автора')
    else:
        print('\t╟')
    if Achieve.link_open > 0:
        print(f'\t╚═> СЁРФЕР: Увидеть логотип Игры, (открытый по ссылке) в браузере ')
    else:
        print('\t╙')
    print('')
    print('\tКОДЕР:\taka. (OPEN-SOURCE code)')
    if Achieve.hello_world > 0:
        print(f'\t╚═> МЕГАХОРОШ: Поменять переменную в окончании файла Игры')
    else:
        print('\t╙X','Подробности в Справке')
    print('')
    waiting()


def about_credits():
    screen_clear()
    print('\n\t\t---/===/ От автора \\===\\---\n')
    print('''\t\t     Здравствуй игрок!\n
    Благодарю тебя за запуск 01_Step, и блока "От автора".
    В этом окошке я в одностороннем порядке желаю тебе удачной игры.\n
    (PS: попробуй ввести "10" в главном меню ;)\n''')
    credits_choose = input('\t>>')
    if credits_choose == '10':
        print('\tДа не здесь! (^-^")')
        Achieve.ten = 1
        waiting()
    Achieve.creditss = 1


def logo_author():
    screen_clear()
    print('\tПожалуйста, увеличь размер окна Игры,')
    print('\tтак ты увидишь то, что нужно ;)')
    input('\tВведи что-нибудь, как будешь готов >> ')
    graphics(10)
    Achieve.logo = 1
    print('''\tЕсли хочешь увидеть ещё графику по
    \t01_Step, то введи "10" ниже :)
    \t(Потребуется подключение к Сети)
    ''')
    if Achieve.link_open:
        Achieve.logo2 = 1
    if Achieve.logo2 != 1:
        print('\t\t(Потом можешь вызвать логотип автора ещё раз ;)')
    choose_open_logo = input('\t>> ')
    if choose_open_logo == '10':
        web.open(link)
        Achieve.link_open = 1
        sleep(1)


def itogi_game(vern,nevern):
    global sum_win, sum_game_over, sum_nichya
    print('\t---===/ ИТОГИ ИГРЫ \\===---')
    print(f'\n\t    ВЕРНЫХ ОТВЕТОВ: {vern}')
    print(f'\t  НЕВЕРНЫХ ОТВЕТОВ: {nevern}\n')
    print('\t  ПОТОМУ', end=' --> ')
    if vern == nevern:
        print("НИЧЬЯ\t:|")
        sum_nichya += 1
    elif vern > nevern:
        print('ПОБЕДА!\t:)')
        sum_win += 1
    else:
        print('ПОРАЖЕНИЕ\t:(')
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
        print(f'\n\t╔═══\t-=/ УРОВЕНЬ {level} \\=-\t═══╗')
        choice_choose = input('\t║Ваше число >>\t')
        try:
            choice_choose = int(choice_choose)
        except ValueError:
            print(necor_zn())
        randomize = (randint(0, 100)%2)
        print(f'\t║Рандом = \t{randomize}')
        if choice_choose == randomize:
            print('\t║ВЕРНО!\t\t√  ')
            vern += 1
        else:
            print('\t║НЕВЕРНО.\tX  ')
            nevern += 1
        print(f'\t╚═══\t-=\\ УРОВЕНЬ {level} /=-\t═══╝\n')
        waiting()
        screen_clear()
    sleep(0.4)
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

    while True:
        numer = input(' Ваше число >> ')
        try:
            numer = int(numer)
            break
        except ValueError:
            print(necor_zn())

    vern = 0
    nevern = 0
    print(f'╔════\t     -=/ ВСЁ ИЛИ НИЧЕГО \\=-\t   ════╗')
    print('║\t| № Ур.\t| Ваш.Ч.| Сл.Ч.\t| +/-  |       ║')
    for level in range(1, lvl + 1):
        randomize = (randint(0, 100) % 2)
        print(f'║\t| {level}\t| {numer}\t| {randomize}\t|',end=' ')
        if numer == randomize:
            print(' √   |       ║')
            vern += 1
        else:
            print(' X   |       ║')
            nevern += 1
        if lvl <= 100:
            sleep(0.05)
        elif lvl <= 1000:
            sleep(0.025)
        else:
            sleep(0.012)
    print(f'╚════\t════════════════════════════════   ════╝\n')
    sleep(0.4)
    print(itogi_game(vern,nevern))
    waiting()


def xp_print(xp):
    print(f'\t\t  {xp}\t', end='')
    for xp_show in range(1, xp + 1):
        if xp_show <= 25:
            if xp_show == 25:
                print('♥ ...')
            elif xp_show == xp:
                print('♥')
            elif xp_show % 5 != 0:
                print('♥', end='')
            else:
                print('♥', end='\n\t\t\t')


def xp_game():
    screen_clear()
    global default_xp, player_xp

    print('\n---/===/\tРЕЖИМ ИГРЫ "ЖИЗНИ"\t\\===\\---\n')
    print('\tКоличество здоровья')
    if default_xp == player_xp:
        print(f'\t(установлено по умолчанию):')
        xp_print(default_xp)
        xp = default_xp
    else:
        print(f'\t(в соответствии с пользовательской настройкой):')
        xp_print(player_xp)
        xp = player_xp
    print('\n\t\t     ПОЕХАЛИ!\n')

    vern = 0
    nevern = 0
    level = 0

    while xp > 0:
        level += 1
        if level > 1:
            xp_print(xp)
        print(f'\t╔═══\t-=/  УРОВЕНЬ {level}   \\=-\t═══╗')
        xp_choose = input('\t║Ваше число >>\t')
        try:
            xp_choose = int(xp_choose)
        except ValueError:
            print(necor_zn())
        randomize = (randint(0, 100) % 2)
        print(f'\t║Рандом = \t{randomize}')
        if xp_choose == randomize:
            print('\t║ВЕРНО!\t\t√  ')
            vern += 1
        else:
            print('\t║НЕВЕРНО.\tX  ')
            nevern += 1
            xp -= 1
        print(f'\t╚═══\t-=\\ Здоровья: {xp} ♥ /=-\t═══╝')
        waiting()
        screen_clear()
    print('\n\tЗДОРОВЬЕ ЗАКОНЧИЛОСЬ!\n')
    sleep(0.4)
    print(itogi_game(vern, nevern))
    waiting()


def podskaz_game():
    screen_clear()
    global default_levels, player_levels
    global default_podskaz, player_podskaz

    print('\n---/===/\tРЕЖИМ ИГРЫ "С ПОДСКАЗКАМИ"\t\\===\\---\n')
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
        randomize = (randint(0, 100) % 2)
        print(f'\n\t╔═══\t-=/ УРОВЕНЬ {level} \\=-\t═══╗')

        if level % pods == 0:
            print(f'\t║РАНДОМ = \t{randomize}')
            podskaz_choose = input('\t║Ваше число !!\t')
            try:
                podskaz_choose = int(podskaz_choose)
            except ValueError:
                print(necor_zn())

        else:
            podskaz_choose = input('\t║Ваше число >>\t')
            try:
                podskaz_choose = int(podskaz_choose)
            except ValueError:
                print(necor_zn())
            print(f'\t║Рандом = \t{randomize}')

        if podskaz_choose == randomize:
            print('\t║ВЕРНО!\t\t√  ')
            vern += 1
        else:
            print('\t║НЕВЕРНО.\tX  ')
            nevern += 1
        print(f'\t╚═══\t-=\\ УРОВЕНЬ {level} /=-\t═══╝\n')
        waiting()
        screen_clear()
    sleep(0.4)
    print(itogi_game(vern,nevern))
    waiting()



# ОСНОВА
base = 'teleport'
while game_restart:
    screen_clear()
    start_window()
    print('\n---/===/\tДОБРО ПОЖАЛОВАТЬ!\t\\===\\---\n')
    if number_zapusk == 1:
        print('''\tИгра запущена первый раз!
        Не желаете-ли прочесть Справку?
        Нажмите "5" для вызова Справки
        ''')
    print('''\t---/===/  ГЛАВНОЕ МЕНЮ:  \\===\\---\t')
    \tВозможные действия:
    \t╠>"1" - Классическая игра
    \t╠>"2" - Режим "Всё или ничего"
    \t╠>"3" - Режим "ЖИЗНИ"
    \t╠>"4" - Режим игры "С подсказками"
    \t╠>"5" - Справка
    \t╠>"6" - Настройки
    \t╠>"7" - Статистика
    \t╠>"8" - Достижения
    \t╠═>"9" - "От автора"
    \t╚>"0" - Выход
    ''')
    print('\t*Все остальные команды перезапускают Игру',end='')
    Achieve.hello_world = 0     # Вот этот 'hello_world' ;)
    if Achieve.logo or Achieve.watch_saves:
        print('**\t\t**Почти все ;)')
    else:
        print('')
    choose = input('\n\t Выбор действия >> ')
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
        exit_global()
        break
    elif choose == '10':
        logo_author()
    elif choose == '11':
        edit_saves()
    else:
        continue
