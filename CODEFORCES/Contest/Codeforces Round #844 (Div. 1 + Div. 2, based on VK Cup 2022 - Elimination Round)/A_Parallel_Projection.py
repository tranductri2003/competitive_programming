t = int(input())
for _ in range(t):
    w, d, h = list(map(int, input().split()))
    a, b, f, g = list(map(int, input().split()))
    res1 = min(h+a+f+abs(b-g), h+b+g+abs(a-f))
    a = w-a
    f = w-f
    b = d-b
    g = d-g
    res2 = min(h+a+f+abs(b-g), h+b+g+abs(a-f))
    print(min(res1, res2))
