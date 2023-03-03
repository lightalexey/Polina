# a = [] a1 a2 a3
a = [5, 45, -45, 0, 5, 6, 7, 0, 54, -90]
print('Первый элемент:', a[0])
n = len(a)
print('количество элементов:', n)
print('Последний элемент:', a[n-1])
print('Последний элемент:', a[-1])

summa = 0
for i in range(n):
    summa += a[i]  # summa = summa + a[i]
print('Сумма всех элементов списка равна', summa)

k = 1
summa = 0
zero = 0
h = 0
l = 0
g = 0
for i in a:
    summa += i  # summa = summa + a[i]
    if i != 0:
        k *= i
    else:
        zero += 1
    if i > 0:
        h += i
        l += 1
    if i % 2 == 0:
        g += 1
print('Сумма всех элементов списка равна', summa)
print('Сумма всех элементов списка равна', sum(a))
print('Произведение ненулевых элементов:', k)
print(sum(a)/n)
print('Количество элементов равных нулю:', zero)
print(h)
print(h/l)
print('Количество четных элементов:', g)
print('Исходный список')
for i in a:
    print(i, end=' ')
print()
for i in range(n):
    print(a[i], end=' ')
print()
print(a)
print(*a)