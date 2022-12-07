
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if 1 in a:
        print("YES")
    else:
        print("NO")
