#  Copyright (c) Vladimir Modenov.
#  Created: 03.09.2022, 16:58
#  Project: StepikPythonProjects
#  File: NumberOfWords.py

# На вход программе подается строка текста, состоящая из слов, разделенных ровно одним пробелом.
# Напишите программу, которая подсчитывает количество слов в ней.

s = input()

print(s.count(' ') + 1)
