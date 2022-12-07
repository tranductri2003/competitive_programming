t = int(input())
for _ in range(t):
    n = int(input())
    f = [0]*(n+3)
    a = list(map(int, input().split()))
    for i in range(1, n+1):
        f[i] = f[i-1]+a[i-1]
    minn = 10**16
    for i in range(1, n+1):
        if f[n] % f[i] == 0:
            kt = True
            pos = i
            temp = i
            for j in range(i+1, n+1):
                if f[j]-f[pos] > f[i]:
                    kt = False
                    break
                elif f[j]-f[pos] == f[i]:
                    temp = max(temp, j-pos)
                    pos = j
            if kt == True:
                minn = min(minn, temp)
    print(minn)
