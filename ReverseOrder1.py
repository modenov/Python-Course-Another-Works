#  Copyright (c) Vladimir Modenov.
#  Created: 21.08.2022, 23:17
#  Project: StepikPythonProjects
#  File: ReverseOrder1.py

# Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.

n = int(input())

while n != 0:
    last_digit = n % 10
    print(last_digit)
    n = n // 10
