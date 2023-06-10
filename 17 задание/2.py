f = open('1_17.txt')
s = f.readlines()
s = [int(x) for x in s]
k = 0
m = 0
l = 0
for i in range(len(s)):
    if 9 < s[i] < 100:
        m = max(s[i], m)

for h in range(len(s) - 1):
    if ((9 < s[h] < 100) and not (9 < s[h + 1] < 100) or (9 < s[h + 1] < 100) and not (9 < s[h] < 100)) and (s[h] + s[h + 1]) % m==0:
        k += 1
        l = max(s[h]+s[h+1],l)
print(k,l)
