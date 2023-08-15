K, L = list(map(int, input().split()))
matrixK = []
for i in range(K):
    matrixK.append([])
    for j in range(K):
        matrixK[i].append(0)
for i in range(K):
    matrixK[i] = list(map(int, input().split()))

N = int(input())
P = list(map(int, input().split()))
