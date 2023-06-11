#Аве, Цезарь 🌶️
#На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными.
#Примечание. Символы, не являющиеся английскими буквами, не изменяются.

text = input().split(' ')
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in text:
    c = 0
    for j in i:
        if j.isalpha():
            c += 1
    for j in i:
        if j.isalpha():
            if j.islower():
                print(eng_lower_alphabet[(eng_lower_alphabet.index(j) + c) % 26], end ='')
            elif j.isupper():
                print(eng_upper_alphabet[(eng_upper_alphabet.index(j) + c) % 26], end = '')
        else:
            print(j, end = '')
    print(' ', end = '')
