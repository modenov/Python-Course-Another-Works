#  Copyright (c) Vladimir Modenov.
#  Created: 14.09.2022, 22:41
#  Project: StepikPythonProjects
#  File: Alphabet.py

# Напишите программу, выводящую следующий список:

myList = []

for i in range(26):
    myList.append(chr(ord('a') + i) * (i + 1))

print(myList)
