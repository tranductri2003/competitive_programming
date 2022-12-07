from collections import defaultdict
N = int(input())

ans = 0
rect = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    if a > b:
        a, b = b, a
    ans = max(ans, a*b/2)
    rect.append((a, b))
# rect.sort(key=lambda rect: -(rect[0]*rect[1]))
rect.sort(reverse=True)
# print(rect)

for i in range(len(rect)-1):
    ans = max(ans, rect[i+1][0]*min(rect[i+1][1], rect[i][1]))


# print(ans)
# temp2 = []
# for i in range(len(rect)-1):
#     nowl = rect[i][0]
#     noww = rect[i][1]

#     thenl = rect[i+1][0]
#     thenw = rect[i+1][1]

#     temp2.append(min(nowl, thenl)*min(noww, thenw))
#     temp2.append(min(nowl, thenw)*min(noww, thenl))

# temp1 = max(data)
# temp2 = max(temp2)
# print(temp1, temp2)
# res = max(temp1, temp2)

ans
if "." not in str(ans):
    ans = str(ans)+".0"


print(ans)
