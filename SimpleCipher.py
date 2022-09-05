#  Copyright (c) Vladimir Modenov.
#  Created: 05.09.2022, 20:50
#  Project: StepikPythonProjects
#  File: SimpleCipher.py

# На вход программе подается строка текста. Напишите программу, которая переводит каждый ее символ
# в соответствующий # ему код из таблицы символов Unicode.

s = input()

for i in range(len(s)):
    print(ord(s[i]), end=" ")
