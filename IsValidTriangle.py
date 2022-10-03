#  Copyright (c) Vladimir Modenov.
#  Created: 03.10.2022, 20:23
#  Project: StepikPythonProjects
#  File: IsValidTriangle.py

# Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных
# числа, и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False
# в противном случае.

# объявление функции
def is_valid_triangle(side1, side2, side3):
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        return True
    else:
        return False


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))
