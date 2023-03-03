a = [5, 45, -450, 0, 5, 6, 7, 0, 54, -90]
print(a)
imax = imin = 0
for i in range(len(a)):
    if a[i] >= a[imax]:
        imax = i
    if a[i] < a[imin]:
        imin = i

print('max:', a[imax], 'index:', imax)
print('min:', a[imin], 'index:', imin)
n = a[0]
a[0] = a[-1]
a[-1] = n
print(a)
n = a[imin]
a[imin] = a[imax]
a[imax] = n
print(a)