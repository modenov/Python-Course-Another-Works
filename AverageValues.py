# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

import math

a = float(input())
b = float(input())

print((a + b) / 2)
print(math.sqrt(a * b))
print((2 * a * b) / (a + b))
print(math.sqrt((a ** 2 + b ** 2) / 2))
