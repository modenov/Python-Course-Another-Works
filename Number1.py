#  Copyright (c) Vladimir Modenov.
#  Created: 27.08.2022, 23:29
#  Project: StepikPythonProjects
#  File: Number1.py

# На вход программе подается одна строка состоящая из цифр.
# Напишите программу, которая считает сумму цифр данной строки.

s = input()
counter = 0

for i in range(0, len(s)):
    counter += int(s[i])

print(counter)
