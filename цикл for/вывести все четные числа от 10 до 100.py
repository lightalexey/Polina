k = 0
for i in range(10, 100):
    if i % 2 == 0:
        print(i, end=' ')
        k = k + 1
print()
for i in range(10, 100, 2):
        print(i, end=' ')
print()
print('количество двухзначных четных чисел равно', k)
k5 = 0
for i in range(10,100):
    if i % 5 == 0:
        k5 = k5 + 1
print(k5)