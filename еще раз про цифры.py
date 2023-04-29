# 1. количество четных цифр
# 2. сумму нечетных цифр
b = input()
k = 0
v = 0
for i in b:
    if int(i) %2==0:
        k+=1
    else:
        v+=int(i)
print(k,v)
