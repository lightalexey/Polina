a = int(input('Введи натуральное число:'))
k = 0
for i in range(1, a+1):
    if a % i == 0:
        k += 1
if k == 2:
     print('число простое')
else:
     print('число составное')

# 2 вариант
k = 0
for i in range(2, a//2+1):
    if a % i == 0:
        k += 1
        break
if k == 0:
     print('число простое')
else:
     print('число составное')

# 3 вариант
k = True
for i in range(2, a//2+1):
    if a % i == 0:
        k = False
        break
if k:
     print('число простое')
else:
     print('число составное')