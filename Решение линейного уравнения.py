#  ax+b=0
a = int(input('a='))
b = int(input('b='))
if a != 0:
    x = -b / a
    print('корень уравнения x=', x)
else:
    if b == 0:
        print('х любое')
    else:
        print('решений нет')
