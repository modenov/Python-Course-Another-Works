#  Copyright (c) Vladimir Modenov.
#  Created: 05.09.2022, 20:41
#  Project: StepikPythonProjects
#  File: CharactersInRange.py

# На вход программе подаются два числа a и b. Напишите программу, которая для каждого кодового значения в
# диапазоне от a до b (включительно), выводит соответствующий ему символ из таблицы символов Unicode.

a = int(input())
b = int(input())

for i in range(a, b + 1):
    print(chr(i), end=' ')
