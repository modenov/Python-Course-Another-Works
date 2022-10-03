#  Copyright (c) Vladimir Modenov.
#  Created: 03.10.2022, 20:41
#  Project: StepikPythonProjects
#  File: CorrectBracketSequence.py

# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из
# символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной
# последовательностью и False в противном случае.

# объявление функции
def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return not text


# считывае
# м данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
