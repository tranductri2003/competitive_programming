t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    print(sum(a)-min(a)-max(a))
