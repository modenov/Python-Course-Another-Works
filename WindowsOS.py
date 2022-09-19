#  Copyright (c) Vladimir Modenov.
#  Created: 19.09.2022, 21:31
#  Project: StepikPythonProjects
#  File: WindowsOS.py

# На вход программе подается одна строка с корректным именем файла в операционной системе Windows. Напишите программу,
# которая разбирает строку на части, разделенные символом "\". Каждую часть вывести в отдельной строке.

line = input()
sepLine = line.split('\\')
print(*sepLine, sep='\n')
