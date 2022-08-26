#  Copyright (c) Vladimir Modenov.
#  Created: 24.08.2022, 20:43
#  Project: StepikPythonProjects
#  File: Table2.py

# Дано натуральное число n (n ≤ 9). Напишите программу, которая печатает таблицу размером n×5,
# где в i-ой строке указано число i (числа отделены одним пробелом).
# На вход программе подается одно натуральное число.

n = int(input())

for i in range(1, n + 1):
    for _ in range(5):
        print(i, end=' ')
    print()

