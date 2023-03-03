a = [5, 4, 5, 100, 2, 6, 17, 0, 9, 4]
print(a)
index1 = 0

for i in range(len(a)-1):
    if a[i] + a[i+1] > a[index1] + a[index1 +1]:
        index1 = i
print(a[index1], a[index1+1])

