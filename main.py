# I just use this file for some example code.

s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')

print()

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[39])

# методы строк
s = 'aabbAAaaccDD'
s = s.lower()
print(s.count('a'))

s = 'www.stepik.org'
print(s.startswith('www'))

s = 'www.stepik.org'
print(s.endswith('.ru'))

s = 'I learn Python language. Python - awesome!'
print(s.find('Python'))

s = '     I learn Python language               '
print(s.strip())

s = 'abcdababa'
print(s.replace('ab', '123'))
