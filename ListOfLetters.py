#  Copyright (c) Vladimir Modenov.
#  Created: 06.09.2022, 22:40
#  Project: StepikPythonProjects
#  File: ListOfLetters.py

# На вход программе подается одно число n. Напишите программу, которая выводит список,
# состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.

n = int(input())

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']

print(abc[:n])
