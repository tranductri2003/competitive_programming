n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a+b
res = len(set(c))
print(res)
