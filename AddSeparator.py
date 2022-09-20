#  Copyright (c) Vladimir Modenov.
#  Created: 20.09.2022, 22:47
#  Project: StepikPythonProjects
#  File: AddSeparator.py

# На вход программе подается строка текста и строка разделитель. Напишите программу, которая вставляет указанный
# разделитель между каждым символом введенной строки текста.

string = input()
separator = input()

print(separator.join(string))
