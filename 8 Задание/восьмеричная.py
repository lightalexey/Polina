k=0
s = '01234567'
ch = '0246'
for i1 in s[1::]:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    b = i1+i2+i3+i4+i5
                    if b.count('6')== 1 and (i1 == '6' and i2 in ch or i2=='6' and i1 in ch and i3 in ch or i3 == '6'and i2 in ch and i4 in ch or i4 =='6' and i3 in ch and i5 in ch or i5 == '6' and i4 in ch):
                        k +=1
print(k)