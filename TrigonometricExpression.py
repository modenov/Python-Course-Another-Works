# Напишите программу, вычисляющую значение тригонометрического выражения
# sinx+cosx+tan2x
# по заданному числу градусов xxx.

import math

x = math.radians(float(input()))
print(math.sin(x) + math.cos(x) + math.tan(x) ** 2)
