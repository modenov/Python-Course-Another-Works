#  Copyright (c) Vladimir Modenov.
#  Created: 19.09.2022, 20:31
#  Project: StepikPythonProjects
#  File: LineByLineOutput.py

# На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.

s = input()
words = s.split()
print(*words, sep='\n')
