# Напишите программу, которая выясняет можно ли из длин строк построить
# возрастающую арифметическую прогрессию.

a = len(input())
b = len(input())
c = len(input())

if  (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0:
    print("YES")
else:
    print("NO")