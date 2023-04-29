b = input()
k = 0
for i in range(len(b)):
    k+=int(b[i])
print(k)
# 2 способ
k = 0
for i in b:
    k += int(i)
print(k)
# 3 способ
b = int(b)
k = 0
while b > 0:
    k += b % 10
    b = b // 10
print(k)