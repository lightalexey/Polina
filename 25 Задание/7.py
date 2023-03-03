for a in range(95632, 95700):
    k = 0
    for b in range(2, a + 1, 2):
        if a % b == 0:
            k += 1
            if k > 6:
                break
    if k == 6:
        #print(a)
        for i in range(2,a+1,2):
            if a % i == 0:
                print(i,end=' ')
        print()
