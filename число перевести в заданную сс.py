number, ss, result = 10, 16, ''  # до 16 сс
while number != 0:
    n = str(number % ss)
    if n == '10':
        n = 'A'
    if n == '11':
        n = 'B'
    if n == '12':
        n = 'C'
    if n == '13':
        n = 'D'
    if n == '14':
        n = 'E'
    if n == '15':
        n = 'F'
    result = n + result
    number //= ss
print(result)  #print(result[::-1])