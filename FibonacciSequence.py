#  Copyright (c) Vladimir Modenov.
#  Created: 14.08.2022, 23:44
#  Project: StepikPythonProjects
#  File: FibonacciSequence.py

# Напишите программу, которая считывает натуральное число n
# и выводит первые nnn чисел последовательности Фибоначчи.

n = int(input())

a = 1
y = 0
for i in range(1, n + 1):
    b = a
    a = b + y
    y = b
    print(b, end=" ")
