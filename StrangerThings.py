#  Copyright (c) Vladimir Modenov.
#  Created: 03.09.2022, 17:20
#  Project: StepikPythonProjects
#  File: StrangerThings.py

# Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди. На приемник ему поступает n различных
# последовательностей кода Морзе. Декодировав их, он получает последовательности из цифр и строчного латинского
# алфавита, при этом во всех сообщениях Оди содержится число 11, причем минимум 3 раза.
# Помогите определить Джиму количество сообщений от Оди.

n = int(input())
counter = 0

for i in range(n):
    s = input()
    if s.count("11") >= 3:
        counter += 1

print(counter)
