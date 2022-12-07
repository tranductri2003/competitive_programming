data = []
for i in range(30):
    s = bin(i)[2:]
    print(i, s, s.count('1'))
    data.append(s.count('1'))
print(data)
