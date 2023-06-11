from random import *
from math import *

play = True

while play: #пока игра идет

    print('\nДобро пожаловать в числовую угадайку! Правила просты: Вам нужно отгадать число и не потерять ваши последние деньги.')


    def max_range(): #проверка макс.числа на правильность
        while True:
            end = input('\nВведите, от 1 до какого конечного числа вы хотите угадывать. (Максимальное число?) ')
            if not end.isdigit() or int(end) < 1:
                print('\nВведите конечное целое число больше нуля!')
                continue
            return int(end)

    maxend = max_range()

    n = randint(1, maxend)

    money = ceil(log2(maxend))

    print('\nВам нужно угадать число от 1 до', maxend, '\n За каждый неверный ответ вам снимают 1 рубль. Ваш баланс:', money, 'руб.')

    def is_valid(a): #Функция проверки введенных данных на корректность
        if a.isdigit():
            a = int(a)
            if 1 <= a <= maxend:
                return True
            else:
                return False

    while True: #защита от дурака, если во время игры будет вводить не целое и не число
        player = input('Введите число: ')
        if not player.isdigit() or not (1 <= int(player) <= maxend):
            print('\nДУРАК! Введи число от 1 до', maxend, '!!!')
            continue
        else:
            player = int(player)

        if player < n:
            money -= 1
            if money < 1:
                print('\nПоздравляю! Вы проиграли все деньги!')
                break
            else:
                print('\nЗагаданное число больше вашего, попробуйте еще разок ;): ')

        elif player > n:
            money -= 1
            if money < 1:
                print('\nПоздравляю! Вы проиграли все деньги!')
                break
            else:
                print('\nЗагаданное число меньше вашего, попробуйте еще разок ;): ')

        elif player == n:
            print('')
            print('\nК сожалению вы угадали!')
            break

    print('Хотите тратить деньги снова?\n Если да, введите "да"\n Если нет, введите тетрагидропиранилциклопентилтетрагидропиридопиридиновые: ')
    answer = input().lower()
    if answer != 'тетрагидропиранилциклопентилтетрагидропиридопиридиновые':
        print('\nЯ вижу вы хотите играть снова :D')
        play = True
    else:
        print('\nмда треш токсик пока')
        play = False

exit = input()