a = None
while a is None:
    try:
        a = int(input('Введите число a: '))
    except:
        print('Введено неверное значение')

f = 1
i = 1

while i < a:
    if f == 1:
        print(i)
        f = 0
    else:
        f = 1
    i += 1

    


    