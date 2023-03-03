a = [1, 45, -45, 14, 47, 1, 4, 0, 47, -12]
a1 = a[0]
a2 = a[1]
a3 = a[2]
for i in range(len(a)-2):
    if a[i]*a[i+1]*a[i+2] > a1*a2*a3:
        a1 = a[i]
        a2 = a[i+1]
        a3 = a[i+2]
print(a1,a2,a3)