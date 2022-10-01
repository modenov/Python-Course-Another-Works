#  Copyright (c) Vladimir Modenov.
#  Created: 01.10.2022, 13:19
#  Project: StepikPythonProjects
#  File: Dividers1.py

# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех
# делителей данного числа.

# объявление функции
def get_factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
