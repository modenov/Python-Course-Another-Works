#  Copyright (c) Vladimir Modenov.
#  Created: 31.08.2022, 23:46
#  Project: StepikPythonProjects
#  File: GoodShade.py

# На вход программе подается строка текста. Напишите программу, которая определяет является ли оттенок
# текста хорошим или нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.

s = input().lower()

if "хорош" in s:
    print("YES")
else:
    print("NO")
