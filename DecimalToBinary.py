#  Copyright (c) Vladimir Modenov.
#  Created: 28.08.2022, 17:40
#  Project: StepikPythonProjects
#  File: DecimalToBinary.py

# На вход программе подается натуральное число, записанное в десятичной системе счисления.
# Напишите программу, которая переводит данное число в двоичную систему счисления.

n = int(input())
string = ''

while n > 0:
    string = str(n % 2) + string
    n //= 2

print(string)
