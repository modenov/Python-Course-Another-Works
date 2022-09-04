#  Copyright (c) Vladimir Modenov.
#  Created: 04.09.2022, 14:02
#  Project: StepikPythonProjects
#  File: com-or-ru.py

# На вход программе подается строка текста. Напишите программу, которая проверяет, что строка заканчивается
# подстрокой # .com или .ru.

s = input()

if s.endswith('.com') or s.endswith('.ru'):
    print("YES")
else:
    print("NO")
