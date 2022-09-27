#  Copyright (c) Vladimir Modenov.
#  Created: 27.09.2022, 23:05
#  Project: StepikPythonProjects
#  File: StarRectangleDef1.py

# Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 10×14 в соответствии
# с образцом.

def draw_box():
    print('*' * 10)
    for i in range(12):
        print('*' + ' ' * 8 + '*')
    print('*' * 10)


# вызов функции
draw_box()
