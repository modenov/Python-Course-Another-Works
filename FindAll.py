#  Copyright (c) Vladimir Modenov.
#  Created: 01.10.2022, 13:43
#  Project: StepikPythonProjects
#  File: FindAll.py

# Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке.
# Проблема заключается в том, что данный метод не находит местоположение всех символов а.

# объявление функции
def find_all(target, symbol):
    return [x for x in range(len(target)) if target[x] == symbol]


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
