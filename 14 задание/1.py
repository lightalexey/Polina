for x in range(15):
    n1 = 5 * 15**0 + x * 15 ** 1 + 3 * 15 ** 2 + 2 * 15 ** 3 + 1 * 15 ** 4
    n2 = 3 * 15**0 + 3 * 15**1 + 2 * 15**2 + x * 15**3 + 1 * 15**4
    n = n1 + n2
    if n % 14 == 0:
        print(n//14)
        break

for x in '0123456789ABCDE':
    if (int('123' + x + '5', 15) + int('1' + x +'233', 15))% 14 == 0:
        print((int('123' + x + '5', 15) + int('1' + x +'233', 15))//14)
        break