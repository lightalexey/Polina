a = int(input('Введи натуральное число:'))
k = 0
for i in range(1, a+1):
    if a % i == 0:
        print(i, end=' ')
        k += 1   # k = k+1 k++
print()
print('количество делителей равно', k)