#  Copyright (c) Vladimir Modenov.
#  Created: 27.08.2022, 23:19
#  Project: StepikPythonProjects
#  File: FIO.py

# На вход программе подаются три строки: имя, фамилия и отчество. Напишите программу,
# которая выводит инициалы человека.

name = input()
middlename = input()
surname = input()

name = name[0]
middlename = middlename[0]
surname = surname[0]

print(name, end="")
print(middlename, end="")
print(surname, end="")
