#  Copyright (c) Vladimir Modenov.
#  Created: 22.09.2022, 23:06
#  Project: StepikPythonProjects
#  File: NumberOfArticles.py

# На вход программе подается строка, содержащая английский текст.
# Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.

s = input().lower().split()

print(f"Общее количество артиклей: {s.count('a') + s.count('an') + s.count('the')}")
