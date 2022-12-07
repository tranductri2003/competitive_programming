from re import X


x = int(input())
left = 1000-x
data = [500, 100, 50, 10, 5, 1]
res = 0

i = 0
while left > 0:
    if left >= data[i]:
        left -= data[i]
        res += 1
    else:
        i += 1

print(res)
