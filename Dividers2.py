#  Copyright (c) Vladimir Modenov.
#  Created: 01.10.2022, 13:35
#  Project: StepikPythonProjects
#  File: Dividers2.py

# Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей
# данного числа.

# объявление функции
def number_of_factors(num):
    return len([i for i in range(1, num + 1) if num % i == 0])


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
