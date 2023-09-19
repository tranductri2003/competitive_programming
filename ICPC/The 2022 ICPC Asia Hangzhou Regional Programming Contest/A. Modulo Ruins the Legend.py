def exgcd(a, b, x, y):
    if b == 0:
        x[0] = 1
        y[0] = 0
        return a
    d = exgcd(b, a % b, x, y)
    t = x[0]
    x[0] = y[0]
    y[0] = t - (a // b) * y[0]
    return d

n, m = map(int, input().split())
A = list(map(int, input().split()))
sum = sum(A) % m
m1 = n % m
m2 = (n * (n + 1)) // 2 % m
s = [0]
d = [0]
a = [0]
b = [0]
m0 = exgcd(m1, m2, s, d)
m3 = exgcd(m0, m, a, b)
s[0] = s[0] * a[0] % m
d[0] = d[0] * a[0] % m
t = (m - sum + m3 - 1) // m3
print((t * m3 + sum) % m)
print((s[0] * t % m + m) % m, (d[0] * t % m + m) % m)
