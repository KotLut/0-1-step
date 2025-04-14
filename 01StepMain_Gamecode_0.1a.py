# ИМПОРТ:
from time import sleep
from random import randint

# ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ:
number_zapusk = 0
game_restart = 1
default_levels = 10
sum_win = 0
sum_game_over = 0
sum_nichya = 0

# ФУНКЦИИ:
def start_window(num_zapusk):
    global number_zapusk
    if num_zapusk <= 1:
        print('ПРИВЕТСТВУЕМ В 0/1-step!')
    else:
        print('ПЕРЕЗАГРУЗКА...')
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
╚═  Запуск        ═╝
    № {number_zapusk}'''
    for stroka in start_win:
        sleep(0.005)
        print(stroka, end='')
    return '\n'


def spravka(spr):
    print('\t-=СПРАВКА=-')
    print('В последующих версиях здесь будет представлена справка.')
    print('Подробная справка.')
    print('Да...')
    return ''


def first_zapusk(zapusk):
    print('Игра запущена первый раз!')
    print('Не желаете ли прочесть Справку?')
    print('Нажмите "2" для вызова Справки')
    print('Чтобы продолжить нажмите любую другую кнопку')
    choose = input()
    if choose == '2':
        print(spravka(True))
        return ''
    return ''

def classic_game(classic):
    global sum_win
    global sum_game_over
    global sum_nichya
    print('---= Классическая игра =---')
    print('Количество уровней', end='')
    if default_levels == 10:
        print(f'(установлено по умолчанию):{default_levels}')
    else:
        print(f'в соответствии с пользовательской настройкой:{default_levels}')
    print('')
    print('ПОЕХАЛИ!')
    print('')

    vern = 0
    nevern = 0
    for level in range(default_levels):
        print('╔══════════════════════════╗')
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
        print('╚══════════════════════════╝')
    print('-=ИТОГИ ИГРЫ=-')
    if vern == nevern:
        print("НИЧЬЯ")
        sum_nichya += 1
    if vern > nevern:
        print('ПОБЕДА!')
        sum_nichya += 1
    else:
        print('ПОРАЖЕНИЕ')
        print('\t:(')
        sum_game_over += 1
    return ''


def global_exit(exitt):
    game_restart = 0
    print('')
    print('ВЫХОД ИЗ ПРОГРАММЫ:')
    print('ЧЕРЕЗ', end=' ')
    for sec in range(7,0,-1):
        if sec == 1:
            print(f'{sec} секунда')
        elif 1 < sec <= 3:
            print(f'{sec} секунды')
        else:
            print(f'{sec} секунд')
        sleep(1)
    return ''


def settings(setting):
    print('Это не готовый раздел.')
    print('Появится в след. обновлениях.')
    return ''


def about_credits(about_me):
    print('Здравствуй игрок, если ты видишь это сообщение, значит ты не случайно сюда зашёл.')
    print('Благодарю тебя за выбор и запуск игры, в частности именно "слова от автора".')
    print('Это то самое окошко в котором я могу в одностороннем порядке пожелать тебе удачной игры.')
    return ''


# ОСНОВА
while game_restart:
    print(start_window(True))
    print('---= ДОБРО ПОЖАЛОВАТЬ! =---')
    if number_zapusk == 1:
        print(first_zapusk(True))
    else:
        print('')
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

