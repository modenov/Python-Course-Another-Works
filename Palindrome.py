#  Copyright (c) Vladimir Modenov.
#  Created: 03.10.2022, 20:39
#  Project: StepikPythonProjects
#  File: Palindrome.py

# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True
# если указанный текст является палиндромом и False в противном случае.

# объявление функции
def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
