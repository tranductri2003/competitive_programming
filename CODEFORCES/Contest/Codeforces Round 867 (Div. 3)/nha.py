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
n = int(input())
for mid in range(0, 10):
    for other in range(1, 10):
        temp = str(other)*n+str(mid)+str(other)*n
        if check(int(temp)):
            res += 1
print(res)
