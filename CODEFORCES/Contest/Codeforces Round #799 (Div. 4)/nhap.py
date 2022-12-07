

def kt(n):
    # cach kho hon
    souoc = 0
    for i in range(1, n+1):
        if i**2 > n:
            break

        if i**2 == n:
            souoc += 1
            break
        if n % i == 0:
            souoc += 2

    if souoc == 2:
        return True
    else:
        return False


n = int(input())
a = list(map(int, input().split()))

snt = 0
for i in range(n):
    if kt(a[i]) == True:
        if a[i] > snt:
            snt = a[i]


print(snt)
for i in range(n):
    if a[i] == snt:
        print(i+1, end=" ")
