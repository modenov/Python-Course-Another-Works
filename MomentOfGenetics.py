#  Copyright (c) Vladimir Modenov.
#  Created: 03.09.2022, 17:03
#  Project: StepikPythonProjects
#  File: MomentOfGenetics.py

# На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин),
# Ц (цитозин), Т (тимин). Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и
# тимина входит в данную строку генетического кода.

gen = input()

print("Аденин:", gen.count('А') + gen.count('а'))
print("Гуанин:", gen.count('Г') + gen.count('г'))
print("Цитозин:", gen.count('Ц') + gen.count('ц'))
print("Тимин:", gen.count('Т') + gen.count('т'))
