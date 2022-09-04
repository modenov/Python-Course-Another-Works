#  Copyright (c) Vladimir Modenov.
#  Created: 04.09.2022, 13:35
#  Project: StepikPythonProjects
#  File: NumberOfDigits.py

# На вход программе подается строка текста.
# Напишите программу, которая подсчитывает количество цифр в данной строке.

# мой вариант
s = input()
counter = 0

for i in range(len(s)):
    if "0" in s[i] or "1" in s[i] or "2" in s[i] or "3" in s[i] or "4" in s[i] or "5" in s[i] or "6" in s[i] or "7" in \
            s[i] or "8" in s[i] or "9" in s[i]:
        counter += 1

print(counter)

# чужой вариант
n = input()
count = 0

for i in range(10):
    count += n.count(str(i))

print(count)