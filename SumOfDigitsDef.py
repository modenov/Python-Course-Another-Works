#  Copyright (c) Vladimir Modenov.
#  Created: 27.09.2022, 23:02
#  Project: StepikPythonProjects
#  File: SumOfDigitsDef.py

# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

def print_digit_sum(num):
    print(sum(int(i) for i in str(num)))


n = int(input())

print_digit_sum(n)
