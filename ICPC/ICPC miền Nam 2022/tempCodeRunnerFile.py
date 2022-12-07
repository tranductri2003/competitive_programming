
s = input()
data = []
nguyenam = ['a', 'e', 'i', 'o', 'u']
so0 = 0
so1 = 0
for i in range(len(s)):
    if s[i] in nguyenam:
        data.append(1)
        so1 += 1
    else:
        data.append(0)
        so0 += 1
res = 0
for i in range(len(data)):
    if data[i] == 1:
        res += so0
        so1 -= 1
    else:
        res += so1
        so0 -= 1
print(res)
