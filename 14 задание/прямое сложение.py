print(bin(4**2020+2**2017-15).count('1'))
# 2 способ
a, b, c = 4**2020+2**2017-15 , 2,''
while a != 0:
    n = str(a%b)
    c += n
    a //= b
print(c.count('1'))
# 3 способ
a, b, c, k = 4**2020+2**2017-15 , 2,'', 0
while a != 0:
    if a % b == 1:
        k += 1
    a //= b
print(k)