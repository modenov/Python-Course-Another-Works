# Напишите программу, которая определяет наименьшее из четырёх чисел.

a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
b = 0
c = 0
if a1 < a2:
    b = a1
else:
    b = a2
if a3 < a4:
    c = a3
else:
    c = a4
if b < c:
    print(b)
else:
    print(c)
