#  Copyright (c) Vladimir Modenov.
#  Created: 03.10.2022, 20:36
#  Project: StepikPythonProjects
#  File: NextPrime.py

# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает
# первое простое число большее числа num.

# объявление функции
def get_next_prime(num):
    num += 1
    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
