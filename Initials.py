#  Copyright (c) Vladimir Modenov.
#  Created: 19.09.2022, 21:05
#  Project: StepikPythonProjects
#  File: Initials.py

# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу,
# которая выводит инициалы человека.

name = input().split()

# first resheniye
for i in range(len(name)):
    print(name[i][0], end='.')

print()

# second resheniye
print(f'{name[0][0]}.{name[1][0]}.{name[2][0]}.')
