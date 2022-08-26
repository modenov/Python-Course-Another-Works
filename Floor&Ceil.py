# Напишите программу, вычисляющую значение x (потолок числа) + x (пол числа)
# по заданному вещественному числу x.

import math

x = float(input())

print(math.floor(x) + math.ceil(x))