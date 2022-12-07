t = int(input())
for _ in range(t):
    n = int(input())
    C = list(map(int, input().split()))
    A = [C[0]]
    B = []
    current = 0

    currentMax = C[0]

    # 0: mang A
    # 1: mang B
    for i in range(1, n):
        if C[i] < C[i-1]:
            if current == 0:
                A.append(C[i])
                currentMax = max(currentMax, C[i])
            else:
                B.append(C[i])
                currentMax = max(currentMax, C[i])
        else:
            if C[i] > currentMax:
                current = 1-current
                if current == 0:
                    A.append(C[i])
                    currentMax = C[i]
                else:
                    B.append(C[i])
                    currentMax = C[i]
            else:
                if current == 0:
                    A.append(C[i])
                    currentMax = max(currentMax, C[i])
                else:
                    B.append(C[i])
                    currentMax = max(currentMax, C[i])
    if A == [] or B == []:
        print(-1)
    else:
        print(len(A))
        print(*A)
        print(len(B))
        print(*B)
