k = 0
for x in range(1, 10):
    for y in range(1, 15):
        if 1/3 ** 0.5 * x + 10 > y > 1 / 3 ** 0.5 * x and x < 5*3**0.5:
            k += 1
print(k)

