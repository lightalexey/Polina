# s = input()
s = 'мама мыла раму!'
print(s[0], len(s), s[len(s)-1], s[-1])
# s[0] = 'М' : так работать не будет!!!
print(s[0:4])
s = 'М' + s[1:]
print(s)
s = 'мама мыла раму!'
s = s.replace('м', 'М', 1)
print(s)
s = s.replace('Мама', 'Папа')
print(s)
s = s.replace('мыла','мыл')
print(s)
k_a = 0
for i in range(len(s)):
    if s[i] == 'а':
        k_a += 1
print(k_a)
k_a = 0
for i in s:
    if i == 'а':
        k_a += 1
print(k_a)
print(s.count('а'))
print((23.0).is_integer())
x=34.0
if x == int(x):
    print(True)
else:
    print(False)
