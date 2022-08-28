#  Copyright (c) Vladimir Modenov.
#  Created: 28.08.2022, 18:07
#  Project: StepikPythonProjects
#  File: InColumn1.py

# На вход программе подается одна строка. Напишите программу, которая выводит элементы строки
# с индексами 0, 2, 4, ... в столбик.

s = input()

for i in range(0, len(s), 2):
    print(s[i])
