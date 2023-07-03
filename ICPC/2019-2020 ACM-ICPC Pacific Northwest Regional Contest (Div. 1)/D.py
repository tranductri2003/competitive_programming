A, B = list(map(int, input().split()))
res = 0
while A != B:
    if A < B:
        A += 1
    else:
        if A % 2 == 0:
            A = A/2
        else:
            A = A+1
    res += 1

print(res)
