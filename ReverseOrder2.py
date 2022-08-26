#  Copyright (c) Vladimir Modenov.
#  Created: 21.08.2022, 23:21
#  Project: StepikPythonProjects
#  File: ReverseOrder2.py

# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.

n = int(input())

while n != 0:
    last_digit = n % 10
    print(last_digit, end='')
    n = n // 10
