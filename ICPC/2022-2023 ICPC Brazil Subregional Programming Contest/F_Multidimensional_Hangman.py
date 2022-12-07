from collections import defaultdict
import sys

input = sys.stdin.readline


N, M = list(map(int, input().split()))
check = defaultdict(lambda: 0)
for _ in range(N):
    s = input()
    pos = s.index("*")
    pre = (s[:pos])
    post = (s[pos+1:])
    for i in range(26):
        temp = str(pre+chr(i+97)+post)
        check[temp] += 1


check = dict(check)
res = max(check.values())
data = []
for num in check:
    temp = (num, check[num])
    data.append(temp)
data.sort(key=lambda x: x[0])
for num in data:
    if num[1] == res:
        print(num[0], num[1])
        break
