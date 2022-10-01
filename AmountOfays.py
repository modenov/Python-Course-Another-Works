#  Copyright (c) Vladimir Modenov.
#  Created: 01.10.2022, 12:39
#  Project: StepikPythonProjects
#  File: AmountOfDays.py

# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней
# в данном месяце.

# объявление функции
def get_days(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 28
    else:
        return ("Ты дурачок?")


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
