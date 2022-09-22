#  Copyright (c) Vladimir Modenov.
#  Created: 22.09.2022, 21:45
#  Project: StepikPythonProjects
#  File: Min&Max.py

# На вход программе подается строка текста, содержащая различные натуральные числа. Из данной строки формируется
# список чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

l = [int(i) for i in input().split()]
x = l.index(min(l))
y = l.index(max(l))
l[x], l[y] = max(l), min(l)

print(*l)
