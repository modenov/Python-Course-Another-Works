#  Copyright (c) Vladimir Modenov.
#  Created: 03.10.2022, 20:42
#  Project: StepikPythonProjects
#  File: SnakeRegister.py

# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре»
# и преобразует его в «змеиный регистр».

# объявление функции
def convert_to_python_case(text):
    return ''.join(['_'+i.lower() if i.isupper() else i.lower() for i in text])[1:]


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
