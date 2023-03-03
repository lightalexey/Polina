k = 0
alphabet = 'ABCDX'
for i1 in alphabet:
    for i2 in alphabet:
        for i3 in alphabet:
            for i4 in alphabet:
                s = i1+i2+i3+i4
                #print(s)
                if s.count('X') == 1:
                    k += 1
print(k)