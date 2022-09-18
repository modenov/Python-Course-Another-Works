#  Copyright (c) Vladimir Modenov.
#  Created: 18.09.2022, 17:19
#  Project: StepikPythonProjects
#  File: NegativesZerosPositives.py

# На вход программе подается натуральное число nn, а затем n целых чисел. Напишите программу, которая сначала
# выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке.
# Числа должны быть выведены в том же порядке, в котором они были введены.

a, b, c = list(), list(), list()

for _ in range(int(input())):
    n = int(input())
    if n > 0:
        a.append(n)
    elif n < 0:
        b.append(n)
    elif n == 0:
        c.append(n)

print(*b, sep='\n')
print(*c, sep='\n')
print(*a, sep='\n')
