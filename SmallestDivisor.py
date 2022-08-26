#  Copyright (c) Vladimir Modenov.
#  Created: 20.08.2022, 23:01
#  Project: StepikPythonProjects
#  File: SmallestDivisor.py

# На вход программе подается число n > 1.
# Напишите программу, которая выводит его наименьший отличный от 1 делитель.

n = int(input())

for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break
