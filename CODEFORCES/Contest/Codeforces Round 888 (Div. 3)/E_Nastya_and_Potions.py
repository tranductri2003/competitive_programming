from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = list(map(int, input().split()))
    phaChe = defaultdict(lambda: [])
    for i in range(n):
