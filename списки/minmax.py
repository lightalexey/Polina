a = [5, 45, -450, 0, 5, 6, 7, 0, 54, -90]
maximum = minimum = a[0]
imax = imin = 0
for i in range(len(a)):
    if a[i] > maximum:
        maximum = a[i]
        imax = i
    if a[i] < minimum:
        minimum = a[i]
        imin = i
print('max:', maximum, 'index:', imax)
print('min:', minimum, 'index:', imin)

