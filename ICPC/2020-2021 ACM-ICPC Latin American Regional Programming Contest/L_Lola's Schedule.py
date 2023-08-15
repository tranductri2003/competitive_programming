from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))


average = sum(a)//n
start = max(a)
for i in range(n):
    if a[i] == start:
        start = i
        break

# Tang
check = defaultdict(lambda: False)
start = start
res1 = 0
holding = a[start % n]
while True:
    if check[start % n] == True:
        break
    else:
        if a[start % n] >= average:
            holding += (a[start % n]-average)
            res1 += (a[start % n]-average)
            print()
        else:
            holding += (average-a[start % n])

            res1 += (average-a[start % n])
        check[start % n] = True
    start += 1
    print(res1)

print(res1)
