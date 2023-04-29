def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return (F(n-1) - F(n-2)) * n

#print(F(8))
sum = 0
for n in range(1, 10 + 1):
    sum += F(n)
print(sum)