a = [5, 2, 5, 0, 2, 6, 7, 0, 9, 4]
k = 0
for i in range(len(a)-2):
    if (a[i] + (a[i + 1])+(a[i+2])) % 2 == 0 and (a[i] % 2 !=0 or a[i + 1] % 2 != 0 or a[i+2]!=0):
        k += 1
print(k)
