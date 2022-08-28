#  Copyright (c) Vladimir Modenov.
#  Created: 28.08.2022, 16:45
#  Project: StepikPythonProjects
#  File: HowMany.py

# На вход программе подается одна строка. Напишите программу, которая определяет сколько раз в строке
# встречаются символы + и *.

s = input()

print(f"Символ + встречается {s.count('+')} раз")
print(f"Символ * встречается {s.count('*')} раз")
