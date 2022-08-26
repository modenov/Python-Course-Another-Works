# программа, которая считывает три числа и подсчитывает количество чётных чисел.
num1, num2, num3 = int(input()), int(input()), int(input())
counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
print("Чётных чисел в введённых вами числах:", counter)