a = [5, 4, 5, 0, 2, 6, 17, 0, 9, 4]
print(a)
a1, a2 = a[0], a[1]

for i in range(len(a)-1):
    if a[i] + a[i+1] > a1 + a2:
        a1 = a[i]
        a2 = a[i+1]
print(a1, a2)

