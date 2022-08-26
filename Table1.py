#  Copyright (c) Vladimir Modenov.
#  Created: 24.08.2022, 18:41
#  Project: StepikPythonProjects
#  File: Table1.py

# Дано натуральное число n (n ≤ 9). Напишите программу, которая печатает таблицу размером n × 3 состоящую
# из данного числа (числа отделены одним пробелом).  На вход программе подается одно натуральное число.

n = int(input())

for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()
