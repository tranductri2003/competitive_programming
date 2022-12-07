N, M = list(map(int, input().split()))
if N % M == 0:
    print(N//M)
else:
    print(N//M+1)
