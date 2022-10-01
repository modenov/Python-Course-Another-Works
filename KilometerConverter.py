#  Copyright (c) Vladimir Modenov.
#  Created: 01.10.2022, 12:32
#  Project: StepikPythonProjects
#  File: KilometerConverter.py

# Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает
# расстояние в милях. Формула для преобразования: мили = километры * 0.6214.

# объявление функции
def convert_to_miles(km):
    result = km * 0.6214
    return result


# считываем данные
num = int(input())

# вызываем функцию
print(round(convert_to_miles(num), 4))
