

n = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(n):
    res += a[i]-(i+1)
if res % 2 == 0:
    print("CPU")
else:
    print("TUAN")
