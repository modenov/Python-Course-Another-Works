#  Copyright (c) Vladimir Modenov.
#  Created: 06.10.2022, 21:30
#  Project: StepikPythonProjects
#  File: CaesarCipher1.py

# Зашифруйте текст «Блажен, кто верует, тепло ему на свете!» алгоритмом Цезаря с сдвигом вправо на 10 символов.

print('Введите "1", если нужно расшифровать текст, либо "2", если нужно зашифровать текст')


def decoding():
    print("Введите число сдвига")
    n = int(input())
    print('Введите строку')
    s = input()
    for i in range(len(s)):
        if s[i].lower() == s[i].upper():
            print(s[i], end='')
        else:
            print(chr(ord(s[i]) - n), end='')


def coding():
    print("Введите число сдвига")
    n = int(input())
    print('Введите строку')
    s = input()
    for i in range(len(s)):
        if s[i].lower() == s[i].upper():
            print(s[i], end='')
        else:
            print(chr(ord(s[i]) + n), end='')


vibor = input()
if vibor == "1":
    decoding()
elif vibor == "2":
    coding()
else:
    print('Ты идиот?')
