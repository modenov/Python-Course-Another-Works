#  Copyright (c) Vladimir Modenov.
#  Created: 03.10.2022, 20:26
#  Project: StepikPythonProjects
#  File: IsNumberPrime.py

# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True
# если число является простым и False в противном случае.

# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
