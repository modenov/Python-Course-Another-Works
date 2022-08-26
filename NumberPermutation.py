# Number permutation
abc = int(input())
digit3 = abc % 10
digit2 = (abc // 10) % 10
digit1 = abc // 100
print(digit1, digit2, digit3, sep='')
print(digit1, digit3, digit2, sep='')
print(digit2, digit1, digit3, sep='')
print(digit2, digit3, digit1, sep='')
print(digit3, digit1, digit2, sep='')
print(digit3, digit2, digit1, sep='')

# not my code
n = int(input())
x = n//100
y = (n//10)%10
c =  n%10
print(x,y,c, sep=("")) 
print(x,c,y, sep=(""))
print(y,x,c, sep=(""))
print(y,c,x, sep=(""))
print(c,x,y, sep=(""))
print(c,y,x, sep=(""))