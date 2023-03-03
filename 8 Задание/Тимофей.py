k = 0
s = 'ТИМОФЕЙ'
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    b = i1+i2+i3+i4+i5
                    if b.count('Т') >= 1 and b.count('Й')<=1:
                       k +=1
print(k)


