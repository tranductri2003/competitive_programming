check = [True]*(10**6+1)
check[0] = False
check[1] = False

i = 2
while i*i <= 10**6:
    if check[i] == True:
        for j in range(i*i, 10**6+1, i):
            check[j] = False
    i += 1


n = int(input())
res = 0
data = []
for i in range(2, n+1):
    if check[i] == True and check[i+2] == True and i+2 <= n:
        res += 1
        data.append((2, i))

print(res)
for pair in data:
    print(pair[0], pair[1])
