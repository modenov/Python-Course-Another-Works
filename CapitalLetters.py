#  Copyright (c) Vladimir Modenov.
#  Created: 31.08.2022, 23:36
#  Project: StepikPythonProjects
#  File: CapitalLetters.py

# На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним пробелом.
# Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.

s = input()
s1 = s.title()

if s == s1:
    print("YES")
else:
    print("NO")
