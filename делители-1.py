#Делители-1
#На вход программе подается два натуральных числа a и b (a < b, a < b). Напишите программу, которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей.
#Формат входных данных
#На вход программе подаются два числа, каждое на отдельной строке.
#Формат выходных данных
#Программа должна вывести два числа на одной строке, разделенных пробелом: число с максимальной суммой делителей и сумму его делителей.

a = int(input())
b = int(input())
m = 0
n = 0
for i in range(a, b+1):
    t = 0
    for j in range(1, i+1):
        if i%j==0:
            t += j
            if t >= m:
                m = t
                n = i
print(n, m, sep=' ')

