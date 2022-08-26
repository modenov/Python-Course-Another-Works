# ищем интересное число!

num = int(input())

a = num % 10
b = (num % 100) // 10
c = num // 100

minimum = min(a, b, c)
maximum = max(a, b, c)
second = (a + b + c) - maximum - minimum

if second == maximum - minimum:
    print("Число интересное")
else:
    print("Число неинтересное")
