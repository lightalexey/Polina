f = open('24_demo.txt')
s = f.read()
# print(len(s))
tec = kmax = 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:  # цепочка растет...
        tec += 1
    else: # цепочка оборвалася..
        #if tec > kmax:
        #    kmax = tec
        kmax = max(kmax, tec)
        tec = 1
#if tec > kmax:
#    kmax = tec
print(max(kmax, tec))