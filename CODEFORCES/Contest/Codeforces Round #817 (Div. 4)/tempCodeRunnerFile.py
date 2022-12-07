a = list(map(int, input().split()))
x = 0
for i in range(0, len(a)):
    x = x ^ a[i]
print(bin(x))
# a.sort()
# x = 0
# for i in range(0, len(a)):
#     x = x ^ a[i]

# print(x)
