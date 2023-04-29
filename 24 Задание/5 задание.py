s = open('24_demo5.txt').read().replace('XYZ', 't').replace('Z', ' ').replace('XX', ' ').replace('YY', ' ').replace('YX', ' ')
s = s.split()
s.sort()
print(s)
