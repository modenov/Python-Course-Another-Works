#  Copyright (c) Vladimir Modenov.
#  Created: 09.10.2022, 21:42
#  Project: StepikPythonProjects
#  File: Pangrams.py

# Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку текста на английском языке и
# возвращает значение True если текст является панграммой и False в противном случае.

def is_pangram(text):
    return set('abcdefghijklmnopqrstuvwxyz') == set(text.lower().replace(' ', ''))


text = input()

print(is_pangram(text))
