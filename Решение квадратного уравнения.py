#  ax^2+bx+c=0
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b - D ** (1 / 2)) / 2 / a
    x2 = (-b + D ** (1 / 2)) / 2 / a
    print('x1=', x1)
    print('x1=', x2)
elif D == 0:
    x = -b / (2 * a)
    print('x1=x2=', x)
else:
    print('действительных решений нет')
