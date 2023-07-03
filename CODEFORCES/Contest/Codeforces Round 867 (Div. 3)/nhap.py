def check(n):
    soUoc = 0
    i = 1
    while i*i <= n:
        if i*i == n:
            soUoc += 1
        else:
            if n % i == 0:
                soUoc += 2
        i += 1
    if soUoc == 2:
        return True
    else:
        return False


res = 0
data = []
N = int(input())
for i in range(1, N+1):
    for j in range(1, N+1):
        if check(i) == True and check(j) == True and check(i+j) and i+j <= N and i <= j:
            res += 1
            data.append((i, j))

print(res)
for pair in data:
    print(pair[0], pair[1])
