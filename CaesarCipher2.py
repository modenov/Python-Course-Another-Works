#  Copyright (c) Vladimir Modenov.
#  Created: 06.10.2022, 21:38
#  Project: StepikPythonProjects
#  File: CaesarCipher2.py

# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.

n = input()

# ищем длину слов переводим в словарь в виде чисел
s = n
for j in n:
    if j in '*,.!@"-':
        s = s.replace(j, '')
g = [len(i) for i in s.split()]

# объявляем переменную счетчик, когда попадается пробел переходим на след ячейку в словаре
count = 0
word_new = ''

for d in n:
    number = ord(d)
    if d == ' ':
        count += 1
        word_new += chr(number)
    elif 65 <= number <= 90:
        number += g[count]
        if number > 90:
            number = number - 26
            word_new += chr(number)
        else:
            word_new += chr(number)
    elif 97 <= number <= 122:
        number += g[count]
        if number > 122:
            number = number - 26
            word_new += chr(number)
        else:
            word_new += chr(number)
    else:
        word_new += chr(number)

print(word_new)
