

for _ in range(int(input())):
    n = int(input())
    Dic = [[] for _ in range(n+1)]

    for _ in range(n-1):
        a, b = map(int, input().split())
        Dic[a].append(b)
        Dic[b].append(a)

    V = [0] * (1+n)
    D = [1]
    A = [0] * (1+n)

    while D:
        n = D[-1]
        if V[n] == 0:
            for a in Dic[n]:
                if V[a] == 0:
                    D.append(a)
            V[n] = 1
            continue

        n = D.pop()
        cnt = 0

        for a in Dic[n]:
            if A[a] == 0:
                continue
            cnt += A[a]

        if cnt == 0:
            cnt = 1
        A[n] = cnt

    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(A[a]*A[b])
