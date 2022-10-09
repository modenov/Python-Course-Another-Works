#  Copyright (c) Vladimir Modenov.
#  Created: 09.10.2022, 21:37
#  Project: StepikPythonProjects
#  File: Month.py

mount_dict = {
'ru': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
       'Декабрь'],
'en': ['January', 'February', 'Marth', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
       'December']
}

# объявление функции
def get_month(language, number):
    return mount_dict[language][number - 1]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
