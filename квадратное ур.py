try:
    a = float(input('введите a:'))
except ValueError:
    print('Введено неверное значение')
try:
    b = float(input('введите b:'))
except ValueError:
    print('Введено неверное значение')
try:
    c = float(input('введите c:'))
except ValueError:
    print('Введено неверное значение')

if a != 0:
    D = (b * b) - (4 * a * c)

    if D == 0:
        print('x = ', -b / (2 * a))
    elif D > 0:
        print('x1 = ', (-b - (D)**0.5) / (2 * a))
        print('x2 = ', (-b + (D)**0.5) / (2 * a))