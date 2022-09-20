#  Copyright (c) Vladimir Modenov.
#  Created: 20.09.2022, 21:58
#  Project: StepikPythonProjects
#  File: CorrectIpAddress.py

# На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой. Напишите программу,
# которая определяет является ли введенная строка текста корректным ip-адресом.

ip = input().split('.')
counter = 0

for i in range(len(ip)):
    if 0 <= int(ip[i]) <= 255:
        counter += 1

if counter == 4:
    print("ДА")
else:
    print("НЕТ")
