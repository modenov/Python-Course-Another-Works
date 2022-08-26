#  Copyright (c) Vladimir Modenov.
#  Created: 13.08.2022, 22:09
#  Project: StepikPythonProjects
#  File: SumOfNumbers2.py

"""
На вход программе подается натуральное число nnn. Напишите программу, которая подсчитывает сумму
тех чисел от 1 до n (включительно) квадрат которых оканчивается на 2, 5 или 8.
"""

n = int(input())
counter = 0

for i in range(1, n + 1):
    if i ** 2 % 10 == 5:
        counter = counter + i

print(counter)
