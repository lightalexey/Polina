for a in range(110203, 110246):
    k = 0
    for b in range(2, a+1):
        if b % 2 == 0 and a % b == 0:
            k += 1
        if k > 4:
            break
    if k == 4:
         #print(a)
         for b in range(2, a + 1):
             if b % 2 == 0 and a % b == 0:
                 print(b, end=' ')
         print()

