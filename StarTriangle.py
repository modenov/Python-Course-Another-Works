#  Copyright (c) Vladimir Modenov.
#  Created: 24.08.2022, 21:20
#  Project: StepikPythonProjects
#  File: StarTriangle.py

# Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный звездный треугольник
# с основанием, равным n в соответствии с примером.

n = int(input())

for i in range(n // 2 + 1):
    for j in range(i + 1):
        print('*', end='')
    print()

for i in range(n // 2, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
