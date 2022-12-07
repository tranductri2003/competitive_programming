n = int(input())
a = list(map(int, input().split()))
so0cuoi = 0
full1 = True
for i in range(1, n-1):
    if a[i] == 0:
        so0cuoi += 1
        full1 = False
    else:
        so0cuoi = 0


if so0cuoi == 0:
    if full1 == True:
        print(1)
    else:
        print(2)
else:
    print(so0cuoi+1)
