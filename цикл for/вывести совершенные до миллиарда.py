for g in range(1,1000000000):
    k = 0
    for i in range(1, g// 2 + 1):
         if g % i == 0:
          k += i
    if k == g:
        print(g)
