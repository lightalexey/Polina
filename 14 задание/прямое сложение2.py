a, b, c = 9**8+3**5-9, 3,''
while a != 0:
    n = str(a%b)
    c += n
    a //= b
print(c.count('2'))
# 2 способ
a, b, c, k =  9**8+3**5-9, 3,'', 0
while a != 0:
    if a % b == 2:
        k += 1
    a //= b
print(k)