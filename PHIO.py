#  Copyright (c) Vladimir Modenov.
#  Created: 27.09.2022, 22:28
#  Project: StepikPythonProjects
#  File: PHIO.py

# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.

# объявление функции
def print_fio(name, surname, patronymic):
    name = name[0]
    surname = surname[0]
    patronymic = patronymic[0]

    print(name, end="")
    print(surname, end="")
    print(patronymic, end="")


# считываем данные
name, surname, patronymic = input().upper(), input().upper(), input().upper()

# вызываем функцию
print_fio(name, surname, patronymic)
