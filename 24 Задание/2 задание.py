f = open('24_demo (2).txt')
s = f.read()
tec = kmax = 1
for i in range(len(s)-1):
    if s[i] == s[i+1] == 'X':
        tec += 1
    else:
        kmax = max(kmax, tec)
        tec = 1
print(max(kmax,tec))