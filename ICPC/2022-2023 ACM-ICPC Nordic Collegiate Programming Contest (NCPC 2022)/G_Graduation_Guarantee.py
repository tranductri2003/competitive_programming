import math
n, k = list(map(int, input().split()))
a = list(map(float, input().split()))

temp = max(a)
data = []
for num in a:
    if num == temp:
        data.append(num)


res = 0
n = len(data)
i = n
while i-(n-i) >= k:
    res += math.comb(n, i)*(temp**i)*((1-temp)**(n-i))
    i -= 1
print(res)
