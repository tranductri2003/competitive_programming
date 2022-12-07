from pickle import FALSE


def check(n):
    souoc = 0
    for i in range(1, n+1):
        if i**2 > n:
            break
        if i**2 == n:
            souoc += 1
        else:
            if n % i == 0:
                souoc += 2
        if souoc > 2:
            return False
    if souoc == 2:
        return True
    else:
        return False


n = int(input())
if check(n):
    print("YES")
else:
    print("NO")
