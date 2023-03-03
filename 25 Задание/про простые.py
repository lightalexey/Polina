for a in range(10**9,10**9+1000):
    k = True
    for b in range(2, int(a**0.5)+1):
        if a % b == 0:
            k = False
            break
    if k:
        print(a)