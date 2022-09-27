#  Copyright (c) Vladimir Modenov.
#  Created: 27.09.2022, 23:08
#  Project: StepikPythonProjects
#  File: StarTriangleDef1.py

# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10 в
# соответствии с образцом:

# объявление функции
def draw_triangle():
    print(*['*' * i for i in range(1, 11)], sep='\n')


# вызов функции
draw_triangle()
