# For each test case, print one integer — the index of the spot where cat B will sleep at hour k.
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    if n % 2 == 0:
        res = k % n
        if res == 0:
            res = n
        print(res)
    else:
        # Moi khi di duoc n//2 buoc thi di them 1 buoc
        di = k-1
        frequency = n//2
        di = di+di//frequency
        pos = 1+di
        pos = pos % n
        if pos == 0:
            print(n)
        else:
            print(pos)
