#  Copyright (c) Vladimir Modenov.
#  Created: 13.08.2022, 22:48
#  Project: StepikPythonProjects
#  File: WithoutZero.py

# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

total = 1

for i in range(10):
    n = int(input())
    if n != 0:
        total = total * n
print(total)
