list = []
A, B, count = None, None, None

while A is None:
    try:
        A = float(input('введите 1 границу: '))
    except ValueError:
        print('Введено неверное значение')

while B is None:
    try:
        B = float(input('введите 2 границу: '))
    except ValueError:
        print('Введено неверное значение')

while count is None:
    try:
        count = float(input('введите счетчик: '))
    except ValueError:
        print('Введено неверное значение')


step = (B-A)/count

print('шаг = ', step)

while A <= B:
    list.append(A)
    A += step

print ('список: ', *list)