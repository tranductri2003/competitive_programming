N, K = list(map(int, input().split()))
if K >= 2*N:
    print(0)
elif K <= N:
    start = 1
    finish = K-1
    print((finish-start+1)//2)
else:
    start = K-N
    finish = N
    print((finish-start+1)//2)
