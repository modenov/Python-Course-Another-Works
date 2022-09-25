#  Copyright (c) Vladimir Modenov.
#  Created: 25.09.2022, 19:33
#  Project: StepikPythonProjects
#  File: InOneLine1.py

# На вход программе подается строка текста, содержащая слова. Напишите программу, которая выводит слова введенной
# строки в столбик.

# first reshenie
s = input().split()
print(*s, sep='\n')

# second reshenie
print(*input().split(), sep='\n')
