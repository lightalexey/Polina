s = [int(i) for i in open('17 (2).txt').readlines()]
k = 0
m = -20001
for i in range(len(s) - 1):
    for j in range(i+1, len(s)):
        if (s[i] % 31 == 0 or s[j] % 31 == 0) and (s[i]-s[j])%2==0:
            k += 1
            m = max(s[i] + s[j], m)
print(k, m)
