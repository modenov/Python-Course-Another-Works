#  Copyright (c) Vladimir Modenov.
#  Created: 28.08.2022, 18:10
#  Project: StepikPythonProjects
#  File: InColumn2.py

# На вход программе подается одна строка. Напишите программу, которая выводит в столбик элементы строки
# в обратном порядке.

s = input()

for i in range(1, len(s) + 1):
    print(s[-i])
