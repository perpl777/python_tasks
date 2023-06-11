
play = True

while play: #пока программа идет

    k = input('Введи шаг сдвига (число больше нуля = шифрование, меньше нуля = дешифрование): ')
    while k.isalpha() or (k[0] != '-' and k[1:].isalpha()) or k == '': #пока шаг не будет цифрой, отрицательной или положительной
        k = input('\nВвести можно только одно положительное или отрицательное число!: ')


    text = input('\nВведи текст, который нужно изменить:\n')
    while text.isspace() or text == '': #пока текст пустой
        text = input('Верно введите текст, который нужно изменить!:\n')
    for i in text: #ё меняем на е
        if i == 'Ё':
            text.replace('Ё', 'Е')
        elif i == 'ё':
            text.replace('ё', 'е')

    #списки алфавитов
    eng_lower_alphabet = [chr(i) for i in range(97, 123)]
    eng_upper_alphabet = [chr(i) for i in range(65, 91)]
    rus_lower_alphabet = [chr(i) for i in range(1072, 1104)]
    rus_upper_alphabet = [chr(i) for i in range(1040, 1072)]

    codetext = ''

    for i in text: #для каждого символа текста
        if i in eng_lower_alphabet:
            codetext += eng_lower_alphabet[(eng_lower_alphabet.index(i) + int(k)) % 26] #добавляем символ в пустой список

        elif i in eng_upper_alphabet:
            codetext += eng_upper_alphabet[(eng_upper_alphabet.index(i) + int(k)) % 26] #по функции index находим место символа

        elif i in rus_lower_alphabet:
            codetext += rus_lower_alphabet[(rus_lower_alphabet.index(i) + int(k)) % 32]

        elif i in rus_upper_alphabet:
            codetext += rus_upper_alphabet[(rus_upper_alphabet.index(i) + int(k)) % 32]

        else: #добавляем пробелы и тд
            codetext += i

    print(codetext)

    again = input('Если нужно зашифровать снова, напишите +:\n')
    if again == '+':
        play = True
    else:
        play = False

exit = input('\nЧтобы выйти нажмите Enter')
