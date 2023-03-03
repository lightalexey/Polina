s = 'через тернии к звездам'
print(s[0],s[-1],len(s))
s = s.replace('ч','Ч',1)+'!'
print(s)
s = 'ч' + s[1:]
print(s)
f = s.count('е')
print(f)
k = 0
for i in range(len(s)):
   if s[i] == 'е':
    k += 1
print(k)
k = 0
for i in range(len(s)):
   if s[i] in 'аоеиуюя':
    k += 1
print(k)