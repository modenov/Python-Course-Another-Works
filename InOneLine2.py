#  Copyright (c) Vladimir Modenov.
#  Created: 25.09.2022, 19:44
#  Project: StepikPythonProjects
#  File: InOneLine2.py

# На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая выводит все
# цифровые символы данной строки.

print(*(i for i in input() if i.isdigit()), sep="")
