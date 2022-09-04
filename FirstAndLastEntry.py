#  Copyright (c) Vladimir Modenov.
#  Created: 04.09.2022, 14:25
#  Project: StepikPythonProjects
#  File: FirstAndLastEntry.py

# На вход программе подается строка текста. Если в этой строке буква «f» встречается только один раз,
# выведите её индекс. Если она встречается два и более раз, выведите индекс её первого и последнего
# вхождения на одной строке, разделенных символом пробела. Если буква «f» в данной строке не встречается,
# следует вывести «NO».

s = input()

if s.count('f') == 1:
    print(s.count('f'))

if s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))

if s.count('f') < 1:
    print("NO")
