for i in range(302300, 10**10, 3023):
    if i % 100 == 21 and str(i)[0] == '1' and str(i)[2:5] == '954' and i % 3023 == 0:
        print(i)