#  Copyright (c) Vladimir Modenov.
#  Created: 04.09.2022, 16:50
#  Project: StepikPythonProjects
#  File: DeletingFragment.py

# На вход программе подается строка текста, в которой буква «h» встречается минимум два раза.
# Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h»,
# а также все символы, находящиеся между ними.

s = input()
s1 = s.find('h')
s2 = s.rfind('h')

s3 = s[s1:s2 + 1]

print(s.replace(s3, ''))
