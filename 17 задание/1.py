# f = open('17.txt')
# s = f.readlines()
# s = [int(i) for i in s]
# print(s)
s = [int(i) for i in open('17.txt').readlines()]
k = 0
m = -20001
#m = -float('inf')
for i in range(len(s) - 1):
    if s[i] % 3 == 0 or s[i + 1] % 3 == 0:
        k += 1
        #if (s[i] + s[i + 1]) > m:
        #    m = s[i] + s[i + 1]
        m = max(s[i] + s[i+1], m)
print(k, m)
