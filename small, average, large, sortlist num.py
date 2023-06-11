arr = []
a = input('введите элемент списка: ')
f = 0

while f == 0:
    arr.append(int(a))
    a = input('введите элемент списка: ')
    if a == 'end':
        f = 1

small = arr[0]
for i in range(1, len(arr)):
    if arr[i] < small:
        small = arr[i]

large = arr[0]
for i in range(1, len(arr)):
    if arr[i] > large:
        large = arr[i]

summa = 0
colvo = 0
for i in range(len(arr)):
    summa += arr[i]
    colvo += 1

avr = summa/colvo
sortlist = []
while len(arr) != 0:
    smalle = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smalle:
            smalle = arr[i]
    sortlist.append(smalle)
    arr.remove(smalle)
    
print('наименьшее число:', small)
print('наибольшее число:', large)
print('среднее число:', avr)
print('упорядоченный список:', sortlist)

