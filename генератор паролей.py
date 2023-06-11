from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

# функции на запрос данных у пользователя
def f1():
    n = input('Сколько нужно паролей? Укажи цифру: ')
    while n.isdigit() == False:
        print('Нужно вводить цифру!')
        n = input('Сколько нужно паролей? Укажи цифру: ')
    return int(n)


def f2():
    l = input('Введите длину пароля: ')
    while l.isdigit() == False:
        print('Нужно вводить цифру!')
        l = input('Введи длину пароля: ')
    return int(l)


def f3():
    add_digit = input('Включить цифры? (д = да, н = нет) ').strip()
    while add_digit.lower() not in ['д', 'н']:
        print('Вводи правильно!')
        add_digit = input('Включить цифры? (д = да, н = нет)').strip()
    return add_digit


def f4():
    add_lowercase = input('Включить прописные буквы? (д = да, н = нет) ').strip()
    while add_lowercase.lower() not in ['д', 'н']:
        print('Вводи правильно!')
        add_lowercase = input('Включить прописные буквы? (д = да, н = нет) ').strip()
    return add_lowercase


def f5():
    add_uppercase = input('Включить строчные буквы? (д = да, н = нет) ').strip()
    while add_uppercase.lower() not in ['д', 'н']:
        print('Вводи правильно!')
        add_uppercase = input('Включить строчные буквы? (д = да, н = нет) ').strip()
    return add_uppercase

def f6():
    add_punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ').strip()
    while add_punctuation.lower() not in ['д', 'н']:
        print('Вводи правильно!')
        add_punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ').strip()
    return add_punctuation

def f7():
    remove_badsymbols = input('Исключить символы il1Lo0O? (д = да, н = нет)').strip()
    while remove_badsymbols.lower() not in ['д', 'н']:
        print('Вводи правильно!')
        remove_badsymbols = input('Исключить символы il1Lo0O? (д = да, н = нет)').strip()
    return remove_badsymbols


# собираем возможные для пользователя символы в кучу
def gen_chars():
    chars = ''

    if add_digit.lower() == 'д':
        chars += digits
    else:
        chars += ''

    if add_lowercase.lower() == 'д':
        chars += lowercase_letters
    else:
        chars += ''

    if add_uppercase.lower() == 'д':
        chars += uppercase_letters
    else:
        chars += ''

    if add_punctuation.lower() == 'д':
        chars += punctuation
    else:
        chars += ''

    if remove_badsymbols.lower() == 'д':
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')
    else:
        chars += ''

    return chars

# делаем пароли
def generate_password():
    for _ in range(n):
        p = ''
        for j in range(l):
            p += choice(chars)
        print(p)

# активация программы
n = f1()
l = f2()
add_digit = f3()
add_lowercase = f4()
add_uppercase = f5()
add_punctuation = f6()
remove_badsymbols = f7()
chars = gen_chars()
generate_password()

exit = input('нажми Enter для выхода')