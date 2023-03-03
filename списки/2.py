a = [5, 45, -45, 0, 5, 6, 7, 0, 54, -90]
maximum = min = a[0]

for i in a:
    if i > maximum:
        maximum = i
    if i < min:
        min = i
print('max:', maximum)
print(min)

print(max(a))
# print(min(a)) так не будет работать
