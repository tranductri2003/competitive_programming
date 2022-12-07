n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
for _ in range(q):
    l, r = list(map(int, input().split()))
    print(a[(l+r)//2])
