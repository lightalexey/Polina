number, ss, result = 10, 16, ''  # до 16 сс
alphabet = '0123456789ABCDEF'
while number != 0:
    n = str(alphabet[number % ss])
    result = n + result
    number //= ss
print(result)  #print(result[::-1])