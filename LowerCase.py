#  Copyright (c) Vladimir Modenov.
#  Created: 01.09.2022, 00:22
#  Project: StepikPythonProjects
#  File: LowerCase.py

# На вход программе подается строка. Напишите программу, которая подсчитывает количество буквенных символов
# в нижнем регистре.

s = input()
s1 = s.lower()
counter = 0

for i in range(len(s)):
    if s[i] == s1[i] and s[i] not in '1234567890':
        counter += 1

print(counter)
